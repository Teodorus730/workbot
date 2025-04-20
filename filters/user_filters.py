from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message

from utils.user_types import load_users


class IsType(BaseFilter):
    def __init__(self, user_type: str) -> None:
        self.user_type = user_type

    async def __call__(self, message: Message) -> bool:
        return message.from_user.username in load_users()[self.user_type]

