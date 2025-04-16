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

