import random
from database.db import request_into_db, request_from_db
from games import Game
import users

#список подарков на барабане

stmnt = """
        select prise_description from prises
        where discount_value = 100 and price_in_scores = 0;
        """
res = request_from_db(stmnt)
gifts = [gift[0] for gift in res]

#список очков на барабане
stmnt = """
        select score from scores;
        """
res = request_from_db(stmnt)
scores = [score[0] for score in res]

#Просмотр списков подарков и очков
def show_gifts():
    print(gifts)

def show_scores():
    print(scores)

drum = list()
drum.extend(gifts)
drum.extend(scores)

#Вращаем барабан. Если забирает приз - конец, если отказ от приза - снова крутим, если очки - угадываем

def make_a_turn():
    is_prise_taken = False
    while not is_prise_taken:
        drum_sector = random.choice(drum)
        print(f"На барабане выпало: {drum_sector}")
        if isinstance(drum_sector, int):
            break
        else:
            end_play = input(f"Забираешь приз или продолжить? д/н: ")
            if end_play == "д":
                is_prise_taken = True
    return drum_sector

