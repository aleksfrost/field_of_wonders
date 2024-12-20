
#Словарик, хранящий слова и описания, а также статистику сложности отгадывания слова
#Состав: Слово:(описание, сложность)
import random


words = {
    "СЕЛЬДЕРЕЙ":("Однолетнее зеленое растение, трава, пряность. Используются листья, стебли и корни", 0),
    "ГРАБЛИ":("Садовый инструмент", 0),
    "МОКРИЦА":("Насекомое с большим количеством ног", 0),
    "ДИКОБРАЗ":("Ежик-переросток", 0),
    "ПОВАРЕЖКА":("Столовый прибор", 0),
}

#получение списка
def get_words():
    for word in words:
        print(f"Слово: {word}",
              f"Описание: {words[word][0]}",
              f"Сложность: {words[word][1]}",
              "----------",
              sep="\n")

#добавление или замена слова
def add_word(word: str, description: str):
    words[word] = (description, 0)
    print(f"Слово '{word}' добавлено.")


#удаление слова
def del_word(word):
     del words[word]
     print(f"Слово '{word}' удалено.")


#вызов при запуске игры, получаем слово и описание
def word_to_guess() -> tuple:
    word, description = random.choice(list(words.items()))
    word_to_show = len(word) * "*"
    return word, description[0], word_to_show

def change_diff(word: str, diff: int):
    words[word] = (word, words[word][0], (words[word][1] + diff) / 2)