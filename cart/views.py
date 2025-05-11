from django.http import HttpRequest

# Create your views here.
from django.shortcuts import render, redirect
from .models import CartItem
from gameplay.models import Prises, Users, UsersPrises


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


def view_cart(request: HttpRequest):
    user = is_authentificated(request)
    cart_items = CartItem.objects.filter(user=is_authentificated(request))
    total_price = sum(item.prise.price_in_scores * item.quantity for item in cart_items)
    scores_to_spend = Users.get_user_stat(user)
    context = {'cart_items': cart_items,
               'total_price': total_price,
               'scores': scores_to_spend,
               }
    return render(request, 'cart/cart.html', context)

def add_to_cart(request, prise_id):
    prise = Prises.objects.get(prise_id=prise_id)
    cart_item, created = CartItem.objects.get_or_create(prise=prise, user=is_authentificated(request))
    cart_item.quantity += 1
    cart_item.save()
    return redirect('exchange')

def remove_from_cart(request: HttpRequest, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')


def add_prises(request: HttpRequest):
    cart_items: list[CartItem] = CartItem.objects.all()
    user = is_authentificated(request)
    to_add = []
    for item in cart_items:
        for _ in range(item.quantity):
            to_add.append((item.user, item.prise))
        users_prises = [UsersPrises(user=u, prise=p) for u, p in to_add]
        res = UsersPrises.objects.bulk_create(users_prises)
        if res:
            CartItem.objects.all().delete()
    return redirect('exchange')
