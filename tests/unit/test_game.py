"""Тестирования работы с базой данных"""

from gameplay.models import Users

import hashlib


def test_get_none_users(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("select * from users")
    result = cursor.fetchone()
    print(result)
    assert result == None



def test_get_only_user(db_connection):
    cursor = db_connection.cursor()
    hashed_password = hashlib.sha256('123456'.encode()).hexdigest()
    user = Users(user_name='Aleks', password=hashed_password, is_admin=True)
    cursor.execute(f"insert into users (user_name, password, is_admin) values ('{user.user_name}', '{user.password}', {user.is_admin} )")
    cursor.execute(f"select user_id from users where user_name = '{user.user_name}'")
    result = cursor.fetchone()
    assert result[0] == 1


def test_get_all_users(db_connection):
    cursor = db_connection.cursor()
    hashed_password = hashlib.sha256('123456'.encode()).hexdigest()
    user1 = Users(user_name='Aleks', password=hashed_password, is_admin=True)
    hashed_password = hashlib.sha256('Bboss123'.encode()).hexdigest()
    user2 = Users(user_name='bigboss', password=hashed_password, is_admin=True)
    cursor.execute(f"insert into users (user_name, password, is_admin) values ('{user1.user_name}', '{user1.password}', {user1.is_admin} )")
    cursor.execute(f"insert into users (user_name, password, is_admin) values ('{user2.user_name}', '{user2.password}', {user2.is_admin} )")
    cursor.execute(f"select * from users")
    result = cursor.fetchall()
    assert len(result) == 2

