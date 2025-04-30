import re
from db_admin.models import Users
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions  import ValidationError


class SignUpForm(forms.Form):
    card_no = forms.IntegerField(max_value=1000000, min_value=100001, label="Номер карты", help_text="Карта лояльности")
    user_name = forms.CharField(max_length=254, min_length=3, label="Имя пользователя")
    password = forms.CharField(max_length=254, min_length=6, label="Пароль")
    confirm_password = forms.CharField(max_length=254, min_length=6, label="Пароль подтв.")


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_pass = cleaned_data.get("confirm_password")

        if password != confirm_pass:
            raise forms.ValidationError("Пароли не совпадают.")


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class GameForm(forms.Form):

    def ru_ru_validator(word):
        print('are we here')
        regex = r'[а-яА-ЯЁё]'
        res = all(map(lambda x: re.findall(regex, x), word))
        print(f'res = {res}')
        if res:
            return word
        else:
            print('Error? Error!')
            raise ValidationError('Только буквы кириллицы, пробел и дефис')

    word = forms.CharField(
        validators=[ru_ru_validator],
        min_length=1,
        required=True,
        label="Введи букву или слово",
        )


    def __str__(self):
        return self.word


