from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter

from utils.user_types import load_users, add_user, del_user, ADMIN
from utils.username_check import username_check

from aiogram.fsm.context import FSMContext
from states.admin_states import AdminSates

from filters.user_filters import IsType
from keyboards.admin_keyboards import make_builder
from messages import adminMessages

admins_router = Router()

# START AND HELP
@admins_router.message(IsType("admins"), Command(commands=["start", "help"]))
async def list_users(msg: Message):
    await msg.answer(adminMessages.help_message)


# LIST USERS
@admins_router.message(IsType("admins"), Command("list_users"))
async def list_users(msg: Message):
    await msg.answer(adminMessages.list_users())


# ADD ADMIN
@admins_router.message(IsType("admins"), Command("add_admin"))
async def add_admin1(msg: Message, state: FSMContext):
    if load_users()["recruts"]:
        await msg.answer(adminMessages.pick_admin, reply_markup=make_builder("recruts").as_markup(
            resize_keyboard=True,
            one_time_keyboard=True)
        )
        return await state.set_state(AdminSates.admin_add_state)
    
    await msg.answer(adminMessages.no_recruts)


@admins_router.message(IsType("admins"), StateFilter(AdminSates.admin_add_state))
async def add_admin2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username not in load_users()["recruts"]:
        return await msg.answer(adminMessages.user_not_found(username))
    
    if add_user(username, "admins"):
        await msg.answer(adminMessages.admin_added(username))
    else:
        await msg.answer(adminMessages.admin_exists(username))
        

# DELETE ADMIN
@admins_router.message(IsType("admins"), Command("del_admin"))
async def del_admin1(msg: Message, state: FSMContext):
    await msg.answer(adminMessages.pick_admin, reply_markup=make_builder("admins").as_markup(
        resize_keyboard=True,
        one_time_keyboard=True)
    )
    return await state.set_state(AdminSates.admin_del_state)
    

@admins_router.message(IsType("admins"), StateFilter(AdminSates.admin_del_state))
async def del_admin2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username == ADMIN:
        return await msg.answer(adminMessages.access_denied)
    
    if del_user(username, "admins"):
        await msg.answer(adminMessages.user_deleted(username))
    else:
        await msg.answer(adminMessages.user_not_found(username))
        

# ADD WORKER
@admins_router.message(IsType("admins"), Command("add_worker"))
async def add_worker1(msg: Message, state: FSMContext):
    if load_users()["recruts"]:
        await msg.answer(adminMessages.pick_worker, reply_markup=make_builder("recruts").as_markup(
            resize_keyboard=True,
            one_time_keyboard=True)
        )
        return await state.set_state(AdminSates.worker_add_state)
    
    await msg.answer(adminMessages.no_recruts)


@admins_router.message(IsType("admins"), StateFilter(AdminSates.worker_add_state))
async def add_worker2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username not in load_users()["recruts"]:
        return await msg.answer(adminMessages.user_not_found(username))
    
    if add_user(username, "workers"):
        await msg.answer(adminMessages.worker_added(username))
    else:
        await msg.answer(adminMessages.worker_exists(username))
        
        
# DELETE WORKER
@admins_router.message(IsType("admins"), Command("del_worker"))
async def del_worker1(msg: Message, state: FSMContext):
    await msg.answer(adminMessages.pick_worker, reply_markup=make_builder("workers").as_markup(
        resize_keyboard=True,
        one_time_keyboard=True)
    )
    return await state.set_state(AdminSates.worker_del_state)
    

@admins_router.message(IsType("admins"), StateFilter(AdminSates.worker_del_state))
async def del_worker2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username == ADMIN:
        return await msg.answer(adminMessages.access_denied)
    
    if del_user(username, "workers"):
        await msg.answer(adminMessages.user_deleted(username))
    else:
        await msg.answer(adminMessages.user_not_found(username))
        

# ADD RECRUT
@admins_router.message(IsType("admins"), Command("add_recrut"))
async def add_recrut1(msg: Message, state: FSMContext):
    await state.set_state(AdminSates.recrut_add_state)
    await msg.answer(adminMessages.add_recrut)


@admins_router.message(IsType("admins"), StateFilter(AdminSates.recrut_add_state))
async def add_recrut2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username_check(username):
        username = username[1:]
    else:
        return await msg.answer(adminMessages.invalid_username)

    if add_user(username, "recruts"):
        await msg.answer(adminMessages.recrut_added(username))
    else:
        await msg.answer(adminMessages.recrut_exists(username))
        
        
# DELETE RECRUT
@admins_router.message(IsType("admins"), Command("del_recrut"))
async def del_recrut1(msg: Message, state: FSMContext):
    await msg.answer(adminMessages.pick_recrut, reply_markup=make_builder("recruts").as_markup(
        resize_keyboard=True,
        one_time_keyboard=True)
    )
    return await state.set_state(AdminSates.recrut_del_state)
    

@admins_router.message(IsType("admins"), StateFilter(AdminSates.recrut_del_state))
async def del_recrut2(msg: Message, state: FSMContext):
    await state.clear()
    
    username = msg.text
    
    if username == ADMIN:
        return await msg.answer(adminMessages.access_denied)
    
    if del_user(username, "recruts"):
        await msg.answer(adminMessages.user_deleted(username))
    else:
        await msg.answer(adminMessages.user_not_found(username))