from utils.user_types import load_users

class adminMessages:
    help_message = \
"""Админ панель
/help - это сообщение
/list_users - список пользователей
/add_admin - добавить админа
/del_admin - удалить админа
/add_worker - добавить работника
/del_worker - удалить работника
/add_recrut - добавить рекрута по нику
/del_recrut - удалить рекрута"""

    no_recruts = "Нет людей для этой работы"
    pick_admin = "Выбери ник админа"
    pick_worker = "Выбери ник работника"
    pick_recrut = "Выбери ник рекрута"
    add_recrut = "Введи ник рекрута через @username"
    invalid_username = "Неправильное имя пользователя"
    
    access_denied = "Доступ запрещен"
    
    def admin_added(username):
        return f"Пользователь {username} добавлен в админы."
    
    def admin_exists(username):
        return f"Пользователь {username} уже является админом."
    
    def worker_added(username):
        return f"Пользователь {username} добавлен в работники."
    
    def worker_exists(username):
        return f"Пользователь {username} уже является работником."
    
    def recrut_added(username):
        return f"Пользователь {username} добавлен в рекруты."
    
    def recrut_exists(username):
        return f"Пользователь {username} уже является рекрутом."
    
    def user_deleted(username):
        return f"Пользователь {username} удален."
    
    def user_not_found(username):
        return f"Пользователь {username} не найден"

    
    def list_users():
        users = load_users()
        text = ""
        for cat in users:
            text += f"{cat}:\n"
            for user in users[cat]:
                text += f"--- @{user}\n"
        return text