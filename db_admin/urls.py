from django.urls import path
from db_admin import views
from gameplay.models import Words

app_name = 'db_admin'


urlpatterns = [
    path('admin_home/', views.admin_home, name='admin_home'),

    path('word', views.WordsListView.as_view(), name='word_list'),
    path('word/new/', views.WordCreateView.as_view(), name='word_create'),
    path('word/<int:pk>/edit/', views.WordUpdateView.as_view(), name='word_update'),
    path('word/<int:pk>/delete/', views.WordDeleteView.as_view(), name='word_delete'),

    path('score', views.ScoresListView.as_view(), name='score_list'),
    path('score/new/', views.ScoreCreateView.as_view(), name='score_create'),
    path('score/<int:pk>/edit/', views.ScoreUpdateView.as_view(), name='score_update'),
    path('score/<int:pk>/delete/', views.ScoreDeleteView.as_view(), name='score_delete'),

    path('prise', views.PrisesListView.as_view(), name='prise_list'),
    path('prise/new/', views.PriseCreateView.as_view(), name='prise_create'),
    path('prise/<int:pk>/edit/', views.PriseUpdateView.as_view(), name='prise_update'),

    path('categorie', views.CategorieListView.as_view(), name='categorie_list'),
    path('categorie/new/', views.CategorieCreateView.as_view(), name='categorie_create'),
    path('categorie/<int:pk>/edit/', views.CategorieUpdateView.as_view(), name='categorie_update'),

    path('card', views.CardListView.as_view(), name='card_list'),

    path('user', views.UserListView.as_view(), name='user_list'),
    path('user/new/', views.UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_update'),

]