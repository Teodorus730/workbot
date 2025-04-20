from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter

from utils.user_types import load_users, add_user, del_user, ADMIN

from aiogram.fsm.context import FSMContext
from states.admin_states import AdminSates

from filters.user_filters import IsType
from keyboards.admin_keyboards import make_builder


admins_router = Router()


@admins_router.message(IsType(load_users()["admins"]), Command("list_users"))
async def list_users(msg: Message):
    users = load_users()
    text = ""
    for cat in users:
        text += f"{cat}:\n"
        for user in users[cat]:
            text += f"--- @{user}\n"
    await msg.answer(text)


@admins_router.message(IsType(load_users()["admins"]), Command("add_admin"))
async def add_admin1(msg: Message, state: FSMContext):
    if load_users()["recruts"]:
        await msg.answer("Выбери ник нового админа", reply_markup=make_builder("recruts").as_markup(
            resize_keyboard=True,
            one_time_keyboard=True)
        )
        return await state.set_state(AdminSates.admin_add_state)
    
    await msg.answer("Нет людей для этой работы")


@admins_router.message(IsType(load_users()["admins"]), StateFilter(AdminSates.admin_add_state))
async def add_admin2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username not in load_users()["recruts"]:
        return await msg.answer("Нет такого")
    
    if add_user(username, "admins"):
        await msg.answer(f"Пользователь {username} добавлен в админы.")
    else:
        await msg.answer(f"Пользователь {username} уже является админом.")
        
        
@admins_router.message(IsType(load_users()["admins"]), Command("del_admin"))
async def del_admin1(msg: Message, state: FSMContext):
    await msg.answer("Выбери ник админа", reply_markup=make_builder("admins").as_markup(
        resize_keyboard=True,
        one_time_keyboard=True)
    )
    return await state.set_state(AdminSates.admin_del_state)
    

@admins_router.message(IsType(load_users()["admins"]), StateFilter(AdminSates.admin_del_state))
async def del_admin2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username == ADMIN:
        return await msg.answer(f"Хуй соси.")
    
    if username not in load_users()["admins"]:
        return await msg.answer("Нет такого")
    
    if del_user(username, "admins"):
        await msg.answer(f"Пользователь {username} удален.")
    else:
        await msg.answer(f"Пользователь {username} не найден.")
        

@admins_router.message(IsType(load_users()["admins"]), Command("add_worker"))
async def add_worker1(msg: Message, state: FSMContext):
    if load_users()["recruts"]:
        await msg.answer("Выбери ник нового работника", reply_markup=make_builder("recruts").as_markup(
            resize_keyboard=True,
            one_time_keyboard=True)
        )
        return await state.set_state(AdminSates.worker_add_state)
    
    await msg.answer("Нет людей для этой работы")


@admins_router.message(IsType(load_users()["admins"]), StateFilter(AdminSates.worker_add_state))
async def add_worker2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username not in load_users()["recruts"]:
        return await msg.answer("Нет такого")
    
    if add_user(username, "workers"):
        await msg.answer(f"Пользователь {username} добавлен в работники.")
    else:
        await msg.answer(f"Пользователь {username} уже является работником.")
        
        
@admins_router.message(IsType(load_users()["admins"]), Command("del_worker"))
async def del_worker1(msg: Message, state: FSMContext):
    await msg.answer("Выбери ник работника", reply_markup=make_builder("workers").as_markup(
        resize_keyboard=True,
        one_time_keyboard=True)
    )
    return await state.set_state(AdminSates.worker_del_state)
    

@admins_router.message(IsType(load_users()["admins"]), StateFilter(AdminSates.worker_del_state))
async def del_worker2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username == ADMIN:
        return await msg.answer(f"Хуй соси.")
    
    if username not in load_users()["workers"]:
        return await msg.answer("Нет такого")
    
    if del_user(username, "workers"):
        await msg.answer(f"Пользователь {username} удален.")
    else:
        await msg.answer(f"Пользователь {username} не найден.")
        
        
@admins_router.message(IsType(load_users()["admins"]), Command("del_recrut"))
async def del_recrut1(msg: Message, state: FSMContext):
    await msg.answer("Выбери ник рекрута", reply_markup=make_builder("recruts").as_markup(
        resize_keyboard=True,
        one_time_keyboard=True)
    )
    return await state.set_state(AdminSates.recrut_del_state)
    

@admins_router.message(IsType(load_users()["admins"]), StateFilter(AdminSates.recrut_del_state))
async def del_recrut2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username == ADMIN:
        return await msg.answer(f"Хуй соси.")
    
    if username not in load_users()["recruts"]:
        return await msg.answer("Нет такого")
    
    if del_user(username, "recruts"):
        await msg.answer(f"Пользователь {username} удален.")
    else:
        await msg.answer(f"Пользователь {username} не найден.")