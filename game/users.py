#Список пользователей
#Имя : очки, [список выбранных скидок]

users = {
    "guest":(0, list()),
}

#Список пользователей
def get_users():
    return list(users)


#Данные пользователя
def get_user(name: str):
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


#Добавление пользователя
def add_user(name: str):
    users[name] = (0, list())
    print(f"Игрок '{name}' добавлен. Начинаем...")
    new_user = get_user(name)
    return new_user

def pref_update(user: str, pref: str):
    users[user][1].append(pref)

def scores_update(user: str, scores: int):
    users[user] = (users.get(user)[0] + scores, users.get(user)[1])