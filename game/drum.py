import random
import users

#список подарков на барабане
gifts = ["Зубная щетка", "Стейк 'Рибай'", "Кружка", "Мыльница", "Бритва", "Колбаса"]

#список очков на барабане
scores = [15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 95, 100]

#Просмотр списков подарков и очков
def show_gifts():
    print(gifts)

def show_scores():
    print(scores)

##########
#Подумать. Редактировать списки смысла нет, можно менять целиком список.
##########

drum = list()
drum.extend(gifts)
drum.extend(scores)

#Вращаем барабан. Если забирает приз - конец, если отказ от приза - снова крутим, если очки - угадываем

def make_a_turn(user):
    is_prise_taken = False
    while not is_prise_taken:
        turn = random.choice(drum)
        print(f"На барабане выпало: {turn}")
        if isinstance(turn, int):
            break
        else:
            to_play = input(f"Забираешь приз или продолжить? д/н: ")
            if to_play == "д":
                users.pref_update(user, turn)
                turn = "prise"
                is_prise_taken = True
    return turn