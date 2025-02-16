
import random
from database.db import request_into_db, request_from_db


class Word:

    def __init__(self, id: int, word: str, description: str, diff: int):
        self.word_id = id
        self.word = word
        self.description = description
        self.difficulty = diff

#получение списка слов
def get_words():
    stmnt = f"""
        select * from words;
        """
    words = [Word(*res) for res in request_from_db(stmnt)]
    return words

#Добавление или замена слова
def add_word(word: str, description: str):
    #words[word] = (description, 0)
    #print(f"Слово '{word}' добавлено.")
    pass

#Удаление слова
def del_word(word):
     #del words[word]
     #print(f"Слово '{word}' удалено.")
    pass

#Вызов при запуске игры, получаем слово и описание
def word_to_guess() -> tuple:
    words = get_words()
    word = random.choice(words)
    word_to_show = len(word.word) * "*"
    return word, word_to_show

def change_diff(word: str, diff: int):
    #words[word] = (word, words[word][0], (words[word][1] + diff) / 2)
    pass
