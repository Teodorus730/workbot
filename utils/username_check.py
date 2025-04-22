import re

def username_check(username: str) -> bool:
    # Убираем @ в начале, если есть
    if username.startswith('@'):
        username = username[1:]
    
    # Проверка длины
    if not (5 <= len(username) <= 32):
        return False

    # Нельзя начинать с цифры
    if username[0].isdigit():
        return False

    # Нельзя содержать двойные подчёркивания
    if '__' in username:
        return False

    # Проверка символов (только латиница, цифры, подчёркивание)
    if not re.fullmatch(r'[A-Za-z0-9_]+', username):
        return False

    return True
