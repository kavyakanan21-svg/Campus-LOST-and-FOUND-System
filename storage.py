import json
import os

items = []
next_id = 1
DATA_FILE = "data/items.json"

def add_item(item):
    global next_id

    item["id"] = next_id
    next_id += 1

    items.append(item)


def get_all_items():
    return items
def update_item_status(item_id, new_status):
    for item in items:
        if item["id"] == item_id:
            item["status"] = new_status
            return True

    return False
def save_items():
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(items, file, indent=4)


def load_items():
    global items, next_id

    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r") as file:
            items = json.load(file)

        if items:
            next_id = max(item["id"] for item in items) + 1
        else:
            next_id = 1

    except (json.JSONDecodeError, OSError):
        items = []
        next_id = 1