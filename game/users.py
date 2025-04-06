#Список пользователей
#Имя : очки, [список выбранных скидок]

import hashlib
from database.db import request_into_db, request_from_db


class User:

    def __init__(self, id=None, name=None, is_admin=False):
        self.user_id = id
        self.user_name = name
        self.is_admin = is_admin


#Список пользователей
def get_users() -> list:
    stmnt = f"""
            select * from users;
            """
    res = request_from_db(stmnt)
    users = [User(id = r[0], name=r[1], is_admin=r[3]) for r in res]
    return users

#Поиск пользователя
def get_user(name: str, password: str) -> User:
    stmnt = f"""
            select user_id, user_name, is_admin
            from users
            where user_name = '{name}' and password = '{password}';
            """
    res = request_from_db(stmnt)[0]
    user = User(*res)

    return user

#Добавление пользователя
def add_user(name: str, password: str) -> User:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    stmnt = f"""
            insert into users(user_name, password)
            values('{name}', '{hashed_password}');
            """
    request_into_db(stmnt)
    user = get_user(name, hashed_password)
    return user

#Авторизация
def auth_user(name: str, password: str) -> User:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if name == "":
        name = 'guest'
        password = 'guest'
        stmnt = f"""
                select user_id, user_name, is_admin
                from users
                where user_name = '{name}';
                """
    else:
        stmnt = f"""
            select user_id, user_name, is_admin
            from users
            where user_name = '{name}' and "password" = '{hashed_password}';
            """
    res = request_from_db(stmnt)
    if res:
        user = User(*res[0])
    else:
        try:
            user = add_user(name, password)
        except Exception:
            return "err"
    return user
