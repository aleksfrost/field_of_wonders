
import random
import string
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
    stmnt = f"""
            insert into words
            (word, description)
            values({word}, {description});
            """
    request_into_db(stmnt)

#Удаление слова
def del_word(word: str):
    if all([w in string.letters for w in word]): #Вынести проверку нужно
        stmnt = f"""
                delete from words
                where word = {word};
                """
    request_into_db(stmnt)

#Вызов при запуске игры, получаем слово и описание
def word_to_guess() -> tuple:
    words = get_words()
    word = random.choice(words)
    word_to_show = len(word.word) * "*"
    return word, word_to_show

def change_diff(word: Word, diff: int):
    previous = word.difficulty
    if diff != 0:
        current = len(word.word) / (len(word.word) - diff)
    else:
        current = 100
    word.difficulty = (previous + current) / 2
    stmnt = f"""
            update words
            set "difficulty" = {word.difficulty}
            where "word_id" = {word.word_id}
            """
    request_into_db(stmnt)


def fill_the_words_test():
    stmnt = """
        insert into words(word, description)
        values
        ('сороконожка', 'насекомое, которое не любит обуваться'),
        ('лейка', 'садовый инвентарь'),
        ('джомолунгма', 'самая высокая гора'),
        ('смехопанорама', 'веселая передача'),
        ('пароход', 'Крузенштерн из простоквашино'),
        ('слякоть', 'неприятная погода на дворе'),
        ('Барселона', 'город, в котором находится известный долгострой')
        ('СЕЛЬДЕРЕЙ','Однолетнее зеленое растение, трава, пряность. Используются листья, стебли и корни'),
        ('ГРАБЛИ','Садовый инструмент'),
        ('МОКРИЦА','Насекомое с большим количеством ног'),
        ('ДИКОБРАЗ','Ежик-переросток'),
        ('ПОВАРЕЖКА','Столовый прибор');

        """

    request_into_db(stmnt)
