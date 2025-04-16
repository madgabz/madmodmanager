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

