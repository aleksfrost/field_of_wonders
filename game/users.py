#Список пользователей
#Имя : очки, [список выбранных скидок]

users = {
    "guest":(0, list()),
}

#Список пользователей
def get_users():
    return list(users)


#Данные пользователя
def auth_user(name: str):
    user = users.get(name)
    if user:
        print(f"Игрок: {name}",
            f"Доступные очки: {users[name][0]}",
            f"Предпочтения: {users[name][1]}",
            sep="\n"
        )
        return name
    else:
        add_user(name)

def get_user_points(name):
    user = users.get(name)
    print(f"Игрок: {name}")
    print(f"Доступные для обмена очки: {user[0]}")

def get_users_stats():
    for user in users:
        print(f"Пользователь: {user}")
        print(f"Предпочтения: {user[1]}")

#Добавление пользователя
def add_user(name: str):
    users[name] = (0, list())
    print(f"Игрок '{name}' добавлен. Начинаем...")
    new_user = auth_user(name)
    return new_user

def pref_update(user: str, pref: str):
    users[user][1].append(pref)

def scores_update(user: str, scores: int):
    users[user] = (users.get(user)[0] + scores, users.get(user)[1])