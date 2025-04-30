# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import hashlib
from django.db import connection, models
from django.db.models import Count, Sum
import random as rnd
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse



class Categories(models.Model):
    categorie_id = models.AutoField(primary_key=True)
    categorie_name = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'categories'


class GameRounds(models.Model):
    gr_id = models.AutoField(primary_key=True)
    game = models.ForeignKey('Games', models.DO_NOTHING, blank=True, null=True)
    round = models.ForeignKey('Rounds', models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'game_rounds'

    def add_game_round(game: 'Games', round: 'Rounds'):
        gr = GameRounds(game=game, round=round)
        gr.save()


class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    letters = models.CharField(max_length=33)
    word = models.ForeignKey('Words', models.DO_NOTHING, blank=False, null=False)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'games'

    def add_game(word: 'Words', user: 'Users') -> 'Games':
        new_game = Games(word=word, user=user)
        new_game.save()
        return new_game

    def update_game_letters(game: 'Games', letters: set):
        letrs = "".join(letters)
        game = Games.objects.filter(pk=game.pk).update(letters=letrs)


    def is_finished(self):
        game_id = self.game_id
        with connection.cursor() as cursor:
            cursor.execute(
                f'''select r.is_word_guessed
                from games g
                join game_rounds gr
                on g.game_id = gr.game_id
                join rounds r
                on gr.round_id = r.round_id
                where g.game_id = {game_id}'''
            )
            result = cursor.fetchall()
        for res in result:
            print(res[0])
            if res[0]:
                return True
        return False

    def get_games_stats():
        with connection.cursor() as cursor:
            cursor.execute(
                f'''
                    select u.user_name "Игрок", sum(r.round_scores) "Очки", count(case when r.is_word_guessed then 1 end) "Победы"
                    from users u
                    join games g
                    on u.user_id = g.user_id
                    join game_rounds gr
                    on g.game_id=gr.game_id
                    join rounds r
                    on gr.round_id = r.round_id
                    group by u.user_name
                    order by 2 desc
                '''
            )
            result = cursor.fetchall()
        return result


class Prises(models.Model):
    prise_id = models.AutoField(primary_key=True)
    prise_description = models.CharField(blank=False, null=False)
    discount_value = models.IntegerField(blank=False, null=False)
    price_in_scores = models.IntegerField(blank=False, null=False)
    categorie = models.ForeignKey(Categories, models.DO_NOTHING, blank=False, null=False)
    to_show = models.BooleanField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'prises'

    def get_coupons():
        prises = Prises.objects.exclude(price_in_scores=0).select_related('categorie').annotate(Count('categorie_id'))
        return prises

    def get_my_coupons(user):
        #prises = UsersPrises.objects.filter(user_id=user.pk).select_related('prise')
        with connection.cursor() as cursor:
            cursor.execute(
                f'''
                    select c.categorie_name, p.prise_description, p.discount_value
                    from users_prises up
                    join users u
                    on up.user_id = u.user_id
                    join prises p
                    on up.prise_id=p.prise_id
                    join categories c
                    on p.categorie_id = c.categorie_id
                    where u.user_id = {user.user_id}
                '''
            )
            result = cursor.fetchall()
        return result
        #return prises


class Rounds(models.Model):
    round_id = models.AutoField(primary_key=True)
    round_scores = models.IntegerField(blank=True, null=True)
    is_word_guessed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'rounds'


    def add_round(game, scores, is_guessed):
        round = Rounds(round_scores=scores, is_word_guessed=is_guessed)
        round.save()
        GameRounds.add_game_round(game, round)


class Scores(models.Model):
    score_id = models.AutoField(primary_key=True)
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scores'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, blank=True, null=True)
    password = models.CharField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    scores = models.BigIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'users'


    def get_by_name(name):
        try:
            user = Users.objects.get(user_name=name)
            return user
        except Users.DoesNotExist:
            return None


    def get_user(name, password):
        hash_pass = hashlib.sha256(password.encode()).hexdigest()
        try:
            user = Users.objects.get(user_name=name, password=hash_pass)
            return user
        except Users.DoesNotExist:
            return None

    def get_hashed_user(name, hash_pass):
        try:
            user = Users.objects.get(user_name=name, password=hash_pass)
            return user
        except Users.DoesNotExist:
            return None


    def add_user(name, password):
        hash_pass = hashlib.sha256(password.encode()).hexdigest()
        user = Users(user_name=name, password=hash_pass)
        user.save()
        return user

    def get_user_stat(user):
        with connection.cursor() as cursor:
            cursor.execute(
                f'''
                    select sum(p.price_in_scores) from users u
                    join users_prises up
                    on u.user_id = up.user_id
                    join prises p
                    on up.prise_id = p.prise_id
                    where u.user_id={user.user_id}
                    group by u.user_id;
                '''
            )
            spent_scores = cursor.fetchone()
            print(spent_scores)
            if spent_scores is None:
                spent_scores = [0]
            cursor.execute(
                f'''
                    select sum(r.round_scores)
                    from users u
                    join games g
                    on u.user_id = g.user_id
                    join game_rounds gr
                    on g.game_id=gr.game_id
                    join rounds r
                    on gr.round_id = r.round_id
                    where u.user_id = {user.user_id}
                    group by u.user_name;
                '''
            )
            scores_total = cursor.fetchone()
            print(scores_total)
            if scores_total is None:
                scores_total = [0]
            scores_to_spend = scores_total[0] - spent_scores[0]
            print(scores_to_spend)
        return scores_to_spend


class Words(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(unique=True)
    description = models.CharField()
    difficulty = models.IntegerField()

    letters = models

    class Meta:
        managed = False
        db_table = 'words'

    def get_word():
        words = Words.objects.all()
        word = rnd.choice(words)
        return word

    def word_to_show(game: Games, letters: set=None, word_hidden: str=None):
        word = Words.objects.get(word_id=game.word_id)
        if word_hidden is None:
            word_hidden = ''.join(len(word.word) * ['*'])
        if letters is None:
            letters = game.letters
        res = []
        count = 0
        for letter in word.word.upper():
            if letter in letters and letter not in word_hidden:
                res.append(letter)
                count += 1
            elif letter in letters and letter in word_hidden:
                res.append(letter)
            else:
                res.append('*')
        return count, ''.join(res)


class UsersPrises(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    prise = models.ForeignKey(Prises, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'users_prises'


class Cards(models.Model):
    card_id = models.IntegerField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards'

    def get_card(card_no):
        try:
            card = Cards.objects.get(card_id=card_no)
            return card
        except Cards.DoesNotExist:
            return None

    def is_card_spare(card_no):
        card = Cards.get_card(card_no)
        print(card)
        if card:
            if card.user_id is None:
                return True
            else:
                raise ValueError(f"Карта {card_no} уже зарегистрирована")
        else:
            raise ValueError("Карты с таким номером не существует.")

