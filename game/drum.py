import random

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

#Вращаем барабан

def make_a_turn():
    turn = random.choice(drum)
    print(f"На барабане выпало: {turn}")
    #return turn


"""
for _ in range(10):
    make_a_turn()
"""