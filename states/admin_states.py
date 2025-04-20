from aiogram.fsm.state import StatesGroup, State


class AdminSates(StatesGroup):
    admin_add_state = State()
    worker_add_state = State()
    admin_del_state = State()
    worker_del_state = State()
    recrut_del_state = State()
    
