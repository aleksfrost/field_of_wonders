import drum
from games import add_game
import words
from users import User, auth_user
from round import Round, add_round, gues_the_word, guess_letter
from prises import get_prise
from database.db import request_into_db, request_from_db
import tables_script
from gui_tkinter.gui_fow import root

fow = root()

#Авторизация
#Возвращает User(user_id, user_name, is_admin)
user_name = input("Добро пожаловать! Введи имя или 'Enter' для входа под гостем: ")
password = input("Добро пожаловать! Введи пароль или 'Enter' для входа под гостем: ")
user = auth_user(user_name, password)


#Запуск главного сценария
word, word_to_show = words.word_to_guess()
game = add_game(word, user)
is_not_guessed = True
while(is_not_guessed):
    print(f"-----------------------------")
    print(f"|      Вращаем барабан      |")
    print(f"-----------------------------")
    print(f"Задание: {word.description}")
    print(f"-----------------------------")
    print(f"Слово: {word_to_show}")
    print(f"-----------------------------")
    drum_turn = drum.make_a_turn()
    round = Round()
    if not isinstance(drum_turn, int):
        prise_id = get_prise(drum_turn)
        print(f"You chose prise: {prise_id}")
        add_round(round, game)
        break
    else:
        to_do = input("Угадать букву (1) или слово (2): ")
        if to_do:
            if to_do == "2":
                try_word = input("Введи слово: ")
                res = gues_the_word(word, try_word)
                if res:
                    round.round_score = drum_turn
                    round.is_word_guessed = res
                    is_not_guessed = False
                    if word_to_show.count("*") / len(word_to_show) == 1:
                        difficulty = 0
                    elif word_to_show.count("*") / len(word_to_show) > 0.6:
                        difficulty = 60
                    elif word_to_show.count("*") / len(word_to_show) > 0.3:
                        difficulty = 30
                    else:
                        difficulty = 100
                    #Call change difficulty fo word -> difficulty
                    add_round(round, game)
                else:
                    print("Неверно. Еще раз")
                    round.round_score = int(res)
                    round.is_word_guessed = res
                    add_round(round, game)

            elif to_do == "1":
                letter = input("Введи букву: ")
                try_letter = guess_letter(word, word_to_show, letter)
                round.letter = letter.lower()
                word_to_show = try_letter[0]
                round.round_score = try_letter[1] * drum_turn
                if "*" not in word_to_show:
                    is_not_guessed = False
                    round.is_word_guessed = True
                add_round(round, game)
print(f"Победа! Загаданное слово: {word.word.upper()}")


"""
users.get_user_points(user)

print()
print("Доступны для обмена скидки:")
for prise in prises:
    pr = prises[prise]
    print(f"{prise}, стоимость баллов: {pr[0]}, скидка: {pr[1]}")
"""

if __name__ == "__main__":
    pass