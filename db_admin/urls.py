from django.urls import path
from db_admin import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("signup", views.signup_view, name="registration"),
    path("login", views.login_view, name="login"),
    path("rules", views.rules_view, name="rules"),
    path("statistics", views.statistics_view, name="statistics"),
    path("exchange", views.exchange_view, name="exchange"),
    path("new_game", views.new_game, name="new_game"),
    path("game_score", views.game_score_view, name="game_score"),
    path("game_prise", views.game_prise_view, name="game_prise"),
    path("game_guess", views.game_guess_view, name="game_guess"),
    path("rotate", views.rotate_drum, name="rotate"),
    path("take_prise", views.take_prise, name="take_prise"),
    path("finish", views.finish_view, name="finish"),
    path("logout", views.logout_view, name="logout"),
]