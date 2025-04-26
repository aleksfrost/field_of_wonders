import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from db_admin.models import Users
from django import forms
from django.core.validators import RegexValidator

#class SignUpForm(UserCreationForm):
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
    # ru_validator = RegexValidator(
    #     regex=r'^[а-яА-Я]',
    #     message='Только буквы русского языка',
    #     code='invalid_ru_ru_input',
    # )

    def ru_ru_validator(word):
        regex = r'[а-яА-ЯЁё]'
        res = all(map(lambda x: re.findall(regex, x), word))
        if res:
            return word
        else:
            raise forms.ValidationError('Только буквы кириллицы, пробел и дефис')

    word = forms.CharField(
        min_length=1,
        required=True,
        validators=[ru_ru_validator,],
        label="Введи букву или слово",
        )


    def __str__(self):
        return self.word


