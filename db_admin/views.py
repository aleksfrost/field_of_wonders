from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from gameplay.models import Words, Users, Scores, Prises, Rounds, Games, Cards, Categories

#all views


def admin_home(request: HttpRequest):
    return render(request, 'db_admin/admin_home.html')


#WORDS
class WordsListView(ListView):
    model = Words
    template_name = 'db_admin/word_list.html'


class WordDetailView(DetailView):
    model = Words
    template_name = 'db_admin/word_detail.html'


class WordCreateView(CreateView):

    model = Words
    template_name = 'db_admin/word_update.html'
    fields = ['word', 'description']

    success_url = reverse_lazy('db_admin:word_list')


class WordUpdateView(UpdateView):

    model = Words
    template_name = 'db_admin/word_update.html'
    fields = ['word', 'description']

    success_url = reverse_lazy('db_admin:word_list')


class WordDeleteView(DeleteView):

    model = Words
    template_name = 'db_admin/word_confirm_delete.html'

    success_url = reverse_lazy('db_admin:word_list')


#SCORES
class ScoresListView(ListView):
    model = Scores
    template_name = 'db_admin/score_list.html'


class ScoreCreateView(CreateView):

    model = Scores
    template_name = 'db_admin/score_update.html'
    fields = ['score']

    success_url = reverse_lazy('db_admin:score_list')


class ScoreUpdateView(UpdateView):

    model = Scores
    template_name = 'db_admin/score_update.html'
    fields = ['score']

    success_url = reverse_lazy('db_admin:score_list')


class ScoreDeleteView(DeleteView):

    model = Scores
    template_name = 'db_admin/score_delete.html'

    success_url = reverse_lazy('db_admin:score_list')


#PRISES
class PrisesListView(ListView):
    model = Prises
    template_name = 'db_admin/prise_list.html'


class PriseCreateView(CreateView):

    model = Prises
    template_name = 'db_admin/prise_update.html'
    fields = ['prise_description', 'discount_value', 'price_in_scores', 'categorie', 'to_show']

    success_url = reverse_lazy('db_admin:prise_list')


class PriseUpdateView(UpdateView):

    model = Prises
    template_name = 'db_admin/prise_update.html'
    fields = ['prise_description', 'discount_value', 'price_in_scores', 'categorie', 'to_show']

    success_url = reverse_lazy('db_admin:prise_list')


#CATEGORIES
class CategorieListView(ListView):
    model = Categories
    template_name = 'db_admin/categorie_list.html'


class CategorieCreateView(CreateView):

    model = Categories
    template_name = 'db_admin/categorie_update.html'
    fields = ['categorie_name']

    success_url = reverse_lazy('db_admin:categorie_list')


class CategorieUpdateView(UpdateView):

    model = Categories
    template_name = 'db_admin/categorie_update.html'
    fields = ['categorie_name']

    success_url = reverse_lazy('db_admin:categorie_list')


#CARDS
class CardListView(ListView):
    model = Cards
    template_name = 'db_admin/cards_list.html'


#USERS
class UserListView(ListView):
    model = Users
    template_name = 'db_admin/user_list.html'


class UserCreateView(CreateView):

    model = Users
    template_name = 'db_admin/user_update.html'
    fields = ['user_name', 'password', 'is_admin']

    success_url = reverse_lazy('db_admin:user_list')


class UserUpdateView(UpdateView):

    model = Users
    template_name = 'db_admin/user_update.html'
    fields = ['is_admin']

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['login'] = self.get_object().user_name
        return context

    success_url = reverse_lazy('db_admin:user_list')
