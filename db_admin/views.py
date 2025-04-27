import hashlib
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import GameForm, SignUpForm, LoginForm
from db_admin.models import Users, Cards, Words, Games, Rounds, Prises, Scores, UsersPrises
from django.forms.models import model_to_dict
import random as rnd


#Набор игровых данных
# class GameStats:
#     def __init__(self, user: Users):
#         self.word: Words = None
#         self.word_show = None
#         self.game: Games = Games.add_game(self.word, user)
#         self.ground: Rounds = None
#         self.letters: set = set()
#         self.status: str = None


#         if self.word is None:
#             self.word = Words.get_word()


#         if self.word_show is None:
#             self.word_show = ''.join(['*']*len(self.word.word))


#Проверка сесии
def is_authentificated(request:HttpRequest):
    data = request.session.get('user')
    if data:
        user = Users.get_hashed_user(data['user_name'], data['password'])
        if user is not None:
            return user
        else:
            return None
    else:
        return None


#Домашняя страница
def home_view(request: HttpRequest):
    user = is_authentificated(request)
    context = {
        'user': user
    }
    return render(request, 'db_admin/home.html', context)


#Регистрация пользователя и карты
def signup_view(request: HttpRequest):
    print("Are we here still?")
    if request.method == 'POST':
        print("Are we here?")
        form = SignUpForm(request.POST)
        if form.is_valid():
            card_no = form.cleaned_data.get("card_no")
            name = form.cleaned_data.get("user_name")
            password = form.cleaned_data.get("password")
            if Cards.is_card_spare(card_no):
                user = Users.get_user(name, password)
                if user is None:
                    user = Users.add_user(name, password)
                    data = model_to_dict(user)
                    request.session['user'] =  data
                card = Cards.get_card(card_no)
                card.user_id = user.user_id
                card.save()             # Сохраняем пару пользователь-карта
            return redirect('home')     # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'db_admin/signup.html', {'form': form})


#Логин
def login_view(request: HttpRequest):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = Users.get_user(username, password)
            if user is not None:
                data = model_to_dict(user)
                request.session['user'] =  data   # Выполняем вход
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'db_admin/login.html', {'form': form})



#Создание новой игры
def new_game(request: HttpRequest):
    user = is_authentificated(request)
    if user is None:
        return redirect('home')
    else:
        word = Words.get_word()
        game: Games = Games.add_game(word, user)
        request.session['game_id'] = str(game.game_id)
        request.session['drum_score'] = None
        request.session['drum_prise'] = None
        request.session['err'] = None
        return redirect("game_score")


#Вращиениебарабана
def rotate_drum(request: HttpRequest):
    prises = Prises.objects.filter(price_in_scores=0)
    scores = Scores.objects.all()
    drum = []
    drum.extend(scores)
    [drum.append(rnd.choice(prises)) for _ in range(5)]
    drum_sector = rnd.choice(drum)
    if isinstance(drum_sector, Scores):
        request.session['drum_score'] = drum_sector.score
        request.session['drum_prise'] = None
        return redirect("game_guess")   #Выпали очки, идем гадать букву или слово
    elif isinstance(drum_sector, Prises):
        request.session['drum_score'] = None
        request.session['drum_prise'] = drum_sector.prise_id
        return redirect("game_prise")   #Выпал приз, брать/не брать
    else:
        raise ValueError('Похоже что барабан сломался :(')  # Выпало что-то совсем не то


#Взять приз
def take_prise(request: HttpRequest):
    prise = Prises.objects.get(prise_id=request.session.get('drum_prise'))
    user = is_authentificated(request)
    user_pr = UsersPrises(user_id=user.pk, prise_id=prise.pk)
    user_pr.save()
    request.session['game_id'] = None
    return redirect('finish')


def game_score_view(request: HttpRequest):
    user = is_authentificated(request)
    if user is None:
        return redirect('home')
    elif request.session.get('game_id') is None:
        return redirect('new_game')
    else:
        game = Games.objects.get(game_id=request.session.get('game_id'))
        if game.is_finished():
            return redirect('home')
        if user.user_id != game.user_id:
            raise ValueError('Данные испорчены')
        else:
            _, word_hidden = Words.word_to_show(game)
            prise = request.session.get('drum_prise')
            score = request.session.get('drum_score')
            if prise is not None:
                prise = Prises.objects.get(prise_id=request.session.get('drum_prise'))
            context = {
                'user': user,
                'word': Words.objects.get(word_id=game.word.word_id),
                'word_to_show': word_hidden,
                'letters': game.letters,
                'score': score,
                'prise': prise,
            }
    return render(request, 'db_admin/game_score.html', context)


def game_prise_view(request: HttpRequest):
    user = is_authentificated(request)
    if user is None:
        return redirect('home')
    elif request.session.get('game_id') is None:
        return redirect('new_game')
    else:
        game = Games.objects.get(game_id=request.session.get('game_id'))
        if game.is_finished():
            return redirect('home')
        if user.user_id != game.user_id:
            raise ValueError('Данные испорчены')
        else:
            letters = set(game.letters)
            _, word_hidden = Words.word_to_show(game, letters)
            prise = request.session.get('drum_prise')
            score = None
            if prise is not None:
                prise = Prises.objects.get(prise_id=request.session.get('drum_prise'))
            context = {
                'user': user,
                'word': Words.objects.get(word_id=game.word.word_id),
                'word_to_show': word_hidden,
                'letters': game.letters,
                'score': score,
                'prise': prise,
            }
    return render(request, 'db_admin/game_prise.html', context)


def game_guess_view(request: HttpRequest):
    user = is_authentificated(request)
    if user is None:
        return redirect('home')
    elif request.session.get('game_id') is None:
        return redirect('new_game')
    else:
        game = Games.objects.get(game_id=request.session.get('game_id'))
        if game.is_finished():
            return redirect('home')
        if user.user_id != game.user_id:
            raise ValueError('Данные испорчены')
        else:
            letters = set(game.letters)
            _, word_hidden = Words.word_to_show(game, letters)
            score = request.session.get('drum_score')
            context = {
                'user': user,
                'word': Words.objects.get(word_id=game.word.word_id),
                'word_to_show': word_hidden,
                'letters': game.letters,
                'score': score,
                'prise': None,
            }
            if request.method == 'POST':
                form = GameForm(request.POST)
                if form.is_valid():
                    request.session['err'] = None
                    word = form.cleaned_data['word'].upper()
                    if len(word) == 1:
                        letters.add(word)
                        Games.update_game_letters(game, letters)
                        count, word_hidden = Words.word_to_show(game, letters, word_hidden)
                        context['word_to_show'] = word_hidden
                        scores = count * score
                        is_guessed = False
                        if '*' not in word_hidden:
                            is_guessed = True
                            Rounds.add_round(game, scores, is_guessed)
                            return redirect('finish', context)
                        Rounds.add_round(game, scores, is_guessed)
                    else:
                        if word.upper() == context.get('word').word.upper():
                            scores = score * len(word)
                            res = word.upper()
                            request.session['clear_word'] = res
                            is_guessed = True
                            Rounds.add_round(game, scores, is_guessed)
                            return redirect('finish')
                else:
                    form = GameForm()
                    context['form'] = form
                    context['err'] = '*Только буквы кириллицы'
                    return render(request, 'db_admin/game_guess.html', context)
                request.session['drum_score'] = None
                return redirect('game_score')
            else:
                form = GameForm()
                context['form'] = form
                return render(request, 'db_admin/game_guess.html', context)



def finish_view(request: HttpRequest):
    prise = None
    pr = request.session.get('drum_prise')
    if pr:
        prise = Prises.objects.get(prise_id=pr)
    word = request.session.get('clear_word')
    context = {
        'prise': prise,
        'word': word
    }
    return render(request, 'db_admin/finish.html', context)


def rules_view(request):
    return render(request, 'db_admin/rules.html')


def statistics_view(request: HttpRequest):
    user = is_authentificated(request)
    if user is None:
        pass
    stats = Games.get_games_stats()
    print(stats)
    context = {'stats': stats}
    return render(request, 'db_admin/statistics.html', context)



def exchange_view(request: HttpRequest):
    user = is_authentificated(request)
    if user is None:
        return redirect(request, 'statistics')
    scores_to_spend = Users.get_user_stat(user)
    prises = Prises.get_coupons()
    context = {
        'scores': scores_to_spend,
        'prises': prises,
        'user': user.user_name,
    }
    return render(request, 'db_admin/exchange.html', context)


def logout_view(request: HttpRequest):
    request.session.clear()
    return redirect('home')