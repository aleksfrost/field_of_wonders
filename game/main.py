import drum
import words
import users
import round


#Коллекция раундов
field_of_wonders = list()


#Авторизация
current_user = input("Добро пожаловать! Введи имя или 'Enter' для входа под гостем: ")
if current_user:
    user = users.get_user(current_user)
else:
    user = users.get_user("guest")


#Запуск главного сценария
word, description, word_to_show = words.word_to_guess()
is_not_guessed = True
round_score = 0
while(is_not_guessed):
    print(f"-------Вращаем барабан-------")
    print(f"Задание: {description}")
    print(f"Слово: {word_to_show}")
    turn = drum.make_a_turn(user)
    if turn == "prise":
        break
    else:
        to_do = input("Угадать букву (б) или слово (с): ")
        if to_do:
            if to_do == "с":
                try_word = input("Введи слово: ")
                res = round.gues_the_word(word, try_word)
                if res:
                    round_score += turn
                    is_not_guessed = False
                    if word_to_show.count("*") / len(word_to_show) == 1:
                        difficulty = 0
                    elif word_to_show.count("*") / len(word_to_show) > 0.6:
                        difficulty = 60
                    elif word_to_show.count("*") / len(word_to_show) > 0.3:
                        difficulty = 30
                    else:
                        difficulty = 100
                    field_of_wonders.append((user, round_score, word, True, difficulty))
                else:
                    print("Неверно. Еще раз")
            elif to_do == "б":
                letter = input("Введи букву: ")
                try_letter = round.guess_letter(word, word_to_show, letter, turn)
                word_to_show = try_letter[0]
                users.scores_update(user, try_letter[1])
                if "*" not in word_to_show:
                    is_not_guessed = False
print(f"Победа! Загаданное слово: {word}")
