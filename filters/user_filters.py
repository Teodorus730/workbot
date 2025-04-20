from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsType(BaseFilter):
    def __init__(self, usernames: List[str]) -> None:
        self.usernames = usernames

    async def __call__(self, message: Message) -> bool:
        print(message.from_user.username, self.usernames)
        return message.from_user.username in self.usernames

