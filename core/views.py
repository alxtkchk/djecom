from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import *


def index(request):
    items = Item.objects.all()
    return render(request, 'main/index.html', {'items': items})


def detail(request):
    item = Item.objects.all()

    return render(request, 'main/indexdetail.html', {'items': item})


def about(request):
    return render(request, 'main/about.html')


def signup(request):
    return render(request, 'registration/signup.html')


@csrf_protect
def signin(request):
    return render(request, 'registration/login.html')


def wishlist(request):
    return render(request, 'main/wishlist.html')


def checkout(request):
    return render(request, 'main/checkout.html')


def cart(request):
    return render(request, 'main/cart.html')
