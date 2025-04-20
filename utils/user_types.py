import json
from pathlib import Path
from config import load_config

config = load_config(".env")

USERS_FILE = Path("storage/users.json")
ADMIN = config.tg_bot.admin_username
DEFAULT_USERS = {
    "workers": [],
    "admins": [ADMIN],
    "recruts": []
}


def load_users() -> dict:
    if not USERS_FILE.exists():
        save_file(DEFAULT_USERS)
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_file(users: dict):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


def add_user(user_id: int, type: str) -> bool:
    users = load_users()
    if user_id not in users[type]:
        users[type].append(user_id)
        save_file(users)
        return True
    return False


def del_user(user_id: int, type: str) -> bool:
    users = load_users()
    if user_id in users[type]:
        users[type].remove(user_id)
        save_file(users)
        return True
    return False
