### File: modmanager/games/example_game.py
def detect(search_dirs):
    for path in search_dirs:
        candidate = path / "Example Game"
        if candidate.exists():
            return {"Example Game": candidate}
    return {}
