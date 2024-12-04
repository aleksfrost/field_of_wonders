#Список пользователей
#Имя : очки, [список выбранных скидок]

users = {
    "Трус":(0, list()),
    "Балбес":(0, list()),
    "Бывалый":(0, list()),
}

#Список пользователей
def get_users():
    return list(users)


#Данные пользователя
def get_user(name: str):
    print(f"Игрок: {name}",
          f"Доступные очки: {users[name][0]}",
          f"Предпочтения: {users[name][1]}",
          sep="\n"
    )