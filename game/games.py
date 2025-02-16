from database.db import request_into_db, request_from_db
from users import User
from words import Word


class Game:

    def __init__(self, id: int = None,  word_id: int = None, user_id: int = None):
        self.game_id = id
        self.word_id = word_id
        self.user_id = user_id


def add_game(word: Word, user: User) -> Game:
    stmnt = f"""
            insert into games(word_id, user_id)
            values({word.word_id}, {user.user_id});
            """
    request_into_db(stmnt)
    game = get_game(word.word_id, user.user_id)
    return game


def get_game(word: int, user: int) -> Game:
    stmnt = f"""
            select * from games
            where word_id = {word} and user_id = {user};
            """
    game = Game(*request_from_db(stmnt)[0])
    return game



