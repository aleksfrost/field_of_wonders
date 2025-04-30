from database.db import request_into_db, request_from_db
from users import User
from words import Word


class Game:

    def __init__(self, id: int = None,  word_id: int = None, user_id: int = None, letters: str = None):
        self.game_id = id
        self.word_id = word_id
        self.user_id = user_id
        self.letters = letters


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
            where word_id = {word} and user_id = {user}
            order by game_id desc;
            """
    game = Game(*request_from_db(stmnt)[0])
    return game

def get_stats():
    stmnt = """
            select u.user_name, sum(r.round_scores) scores, count(case when r.is_word_guessed then 1 end) wins from users u
            join games g on u.user_id = g.user_id
            join game_rounds gr on g.game_id = gr.game_id
            join rounds r on r.round_id = gr.round_id
            group by u.user_name;
            """
    stats = request_from_db(stmnt)
    print(stats)
    return stats
