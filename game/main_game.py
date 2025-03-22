import drum
from games import add_game, Game
from words import Word, word_to_guess, change_diff
from ground import gRound, add_round, gues_the_word, guess_letter
from prises import get_prise
from users import User

class GameData:
    def __init__(self, word: Word, word_to_show: str, user: User, game: Game):
        self.word: Word = word
        self.word_to_show: str = word_to_show
        self.user: User = user
        self.game: Game = game
        self.ground: gRound = None
        self.letters: set = set()
        self.status: str = None


def create_game(user: User) -> GameData:
    word, word_to_show = word_to_guess()
    game = add_game(word, user)
    game_data = GameData(word, word_to_show, user, game)
    return game_data


def turn_the_drum(game_data: GameData) -> GameData:
    drum_sector = drum.make_a_turn()
    ground = gRound()
    if isinstance(drum_sector, int):
        ground.round_score = drum_sector
    else:
        ground.round_prise = drum_sector
    game_data.ground = ground
    return game_data


def guess_a_letter(letter, game_data: GameData) ->GameData:
    try_letter = guess_letter(game_data.word, game_data.word_to_show, letter)
    game_data.letters.add(letter.upper())
    game_data.word_to_show = try_letter[0]
    game_data.ground.round_score = game_data.ground.round_score * try_letter[1]
    if "*" not in game_data.word_to_show:
        game_data.ground.is_word_guessed = True
        add_round(game_data)
        update_word(game_data)
        print(f"Победа! Загаданное слово: {game_data.word_to_show.upper()}")
    else:
        game_data.ground.is_word_guessed = False
        add_round(game_data)
    return game_data


def guess_the_word(word: str, game_data: GameData):
    res = gues_the_word(game_data.word, word)
    if res:
        game_data.ground.is_word_guessed = res
        add_round(game_data)
        update_word(game_data)
        print(f"Победа! Загаданное слово: {game_data.word.word.upper()}")
    else:
        game_data.ground.round_score = int(res)
        add_round(game_data)
        print("Неверно. Еще раз")
    return game_data


def update_word(game_data: GameData):
    change_diff(game_data.word, len(game_data.letters))
