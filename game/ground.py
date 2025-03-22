
from database.db import request_from_db, request_into_db

from words import Word

import typing

if typing.TYPE_CHECKING:
    from main_game import GameData

class gRound:

    def __init__(self):
        self.round_id: int = None
        self.round_score: int = 0
        self.round_prise: str = None
        self.is_word_guessed = False

def add_game_round(round_id: int, game_id: int):
    stmnt = f"""
            insert into game_rounds(game_id, round_id)
            values({game_id}, {round_id})
            ;
            """
    request_into_db(stmnt)

def add_round(game_data: 'GameData'):
    stmnt = f"""
            insert into rounds(round_scores, is_word_guessed)
            values(
                {game_data.ground.round_score},
                {game_data.ground.is_word_guessed})
            ;
            """
    request_into_db(stmnt)
    stmnt = """
            select round_id from rounds
            order by round_id desc
            ;
            """
    r_id = request_from_db(stmnt)[0][0]
    add_game_round(r_id, game_data.game.game_id)

#Сравниваем слова, да/нет
def gues_the_word(word: Word, try_word: str):
    equality = (False, True)[word.word.upper() == try_word.upper()]
    return equality

# проверяем букву
def guess_letter(word: Word, word_to_show: str, letter: str):
    if letter and len(letter) == 1:
        letter = letter.upper()
        the_word = word.word.upper()
        print(the_word)
        print(word_to_show)
        count = 0
        word_fabric = []
        for i in range(len(the_word)):
            if the_word[i] == letter:
                word_fabric.append(letter)
                count += 1
            else:
                if word_to_show[i] != "*":
                    word_fabric.append(word_to_show[i])
                else:
                    word_fabric.append("*")
        word_to_show = "".join(word_fabric)
        print(word_to_show)
    return word_to_show, count
