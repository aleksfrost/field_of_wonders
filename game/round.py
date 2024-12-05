#Сравниваем слова, да/нет
def gues_the_word(word: str, try_word: str):
    return (False, True)[word == try_word.upper()]

# проверяем букву
def guess_letter(word: str, word_to_show: str, letter: str, turn: int):
    if letter and len(letter) == 1:
        letter = letter.upper()
        count = 0
        word_fabric = []
        for i in range(len(word)):
            if word[i] == letter:
                word_fabric.append(letter)
                count += 1
            else:
                if word_to_show[i] != "*":
                    word_fabric.append(word_to_show[i])
                else:
                    word_fabric.append("*")
        word_to_show = "".join(word_fabric)
        print(f'scores = {count} * {turn}')
        scores = count * turn
    else:
        scores = 0
    return word_to_show, scores
