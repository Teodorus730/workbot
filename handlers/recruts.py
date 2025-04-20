from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from utils.user_types import add_user

recruts_router = Router()


@recruts_router.message(Command("work"))
async def add_recrut(msg: Message):
    uname = msg.from_user.username
    if not uname:
        await msg.answer(f"Нет ника")
        
    if add_user(uname, "recruts"):
        await msg.answer(f"Ваша заявка отправлена")
    else:
        await msg.answer(f"Ваша заявка уже есть")


    