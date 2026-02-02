import json
from pathlib import Path
from typing import List
from app.schemas.menu import MenuItem


MENU_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_menu.json"


def load_menu() -> List[MenuItem]:
    with open(MENU_PATH, "r") as f:
        raw_items = json.load(f)

    return [MenuItem(**item) for item in raw_items]
