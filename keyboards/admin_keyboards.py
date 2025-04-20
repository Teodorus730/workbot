from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton
from utils.user_types import load_users


def make_builder(type: str):
    builder = ReplyKeyboardBuilder()
    for user in load_users()[type]:
        builder.add(KeyboardButton(text=str(user)))
    builder.adjust(4)
    
    return builder
