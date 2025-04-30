from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:prise_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_prises', views.add_prises, name='add_prises'),
]