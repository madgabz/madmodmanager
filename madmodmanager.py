### File: madmodmanager/app.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from modmanager.core.game_manager import find_installed_games

class ModManagerApp(toga.App):
    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        self.game_list = toga.Selection(items=[], style=Pack(padding=10))
        self.main_box.add(self.game_list)

        self.games = find_installed_games()
        self.game_list.items = list(self.games.keys())

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

def main():
    return ModManagerApp('Mod Manager', 'com.example.modmanager')


### File: modmanager/core/game_manager.py
import os
from pathlib import Path

def find_installed_games():
    search_dirs = [
        Path.home() / ".steam/steam/steamapps/common",
        Path("/usr/games"),
        Path("/opt")
    ]

    found_games = {}

    from modmanager.games import example_game
    found_games.update(example_game.detect(search_dirs))

    return found_games


### File: modmanager/games/example_game.py
def detect(search_dirs):
    for path in search_dirs:
        candidate = path / "Example Game"
        if candidate.exists():
            return {"Example Game": candidate}
    return {}


### File: tests/test_game_manager.py
from modmanager.core.game_manager import find_installed_games

def test_find_installed_games():
    games = find_installed_games()
    assert isinstance(games, dict)


### File: setup.py
from setuptools import setup, find_packages

setup(
    name='modmanager',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'toga>=0.4.0'
    ],
    entry_points={
        'console_scripts': [
            'modmanager = modmanager.app:main',
        ],
    },
)


### File: requirements.txt
toga>=0.4.0


### File: .gitignore
__pycache__/
build/
dist/
*.egg-info/
*.pyc


### File: README.md
# ModManager

A lightweight, cross-platform mod manager for games on Linux, with support for modular game detection and mod handling. Inspired by Nexus Mod Manager.

## Features
- Detect installed games (Linux first)
- Modular game support
- UI built with Python + Toga
- OS-agnostic design

## Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/modmanager.git
cd modmanager
pip install -e .
modmanager
```

## License
MIT


### File: LICENSE
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
