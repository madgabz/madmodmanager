### File: tests/test_game_manager.py
from modmanager.core.game_manager import find_installed_games

def test_find_installed_games():
    games = find_installed_games()
    assert isinstance(games, dict)

