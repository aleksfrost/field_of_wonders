
import hashlib
from django import forms
from django.http import HttpRequest
from gameplay.forms import SignUpForm
from gameplay.models import Users
from gameplay.views import signup_view


def test_signin_card_tamed(request: HttpRequest, db_connection):
    cursor = db_connection.cursor()
    hashed_password = hashlib.sha256('123456'.encode()).hexdigest()
    user = Users(user_name='Aleks', password=hashed_password, is_admin=True)
    cursor.execute(f"insert into users (user_name, password, is_admin) values ('{user.user_name}', '{user.password}', {user.is_admin} )")
    cursor.execute(f"select user_id from users where user_name = '{user.user_name}'")
    result = cursor.fetchone()
    cursor.execute(f"insert into cards (card_id, user_id) values ({100001}, {result[0]})")


    form = SignUpForm(request.POST)
    form.card_no = 100001
    form.user_name = 'Bob'
    form.password = 'Bob123456'
    form.confirm_password = 'Bob123456'
    request.POST = form.__dict__
    assert signup_view(request) == ValueError(f"Карта {form.card_no} уже зарегистрирована")


def test_signin_card_not_exist(request: HttpRequest, db_connection):
    cursor = db_connection.cursor()
    request.method = 'POST'
    form = SignUpForm(request.POST)
    form.card_no = 200002
    form.user_name = 'Bob'
    form.password = 'Bob123456'
    form.confirm_password = 'Bob123456'
    assert signup_view(request) == ValueError(f"Карты с номером {form.card_no} не существует.")


def test_signin_incorrect_pass(request: HttpRequest, db_connection):
    cursor = db_connection.cursor()
    request.method = 'POST'
    form = SignUpForm(request.POST)
    form.card_no = 200002
    form.user_name = 'Bob'
    form.password = 'Bob123456'
    form.confirm_password = 'Bub123456'
    assert signup_view(request) == forms.ValidationError("Пароли не совпадают")


def test_signin_correct_data(request: HttpRequest, db_connection):
    cursor = db_connection.cursor()
    request.method = 'POST'
    form = SignUpForm(request.POST)
    form.card_no = 200002
    form.user_name = 'Bob'
    form.password = 'Bob123456'
    form.confirm_password = 'Bob123456'



