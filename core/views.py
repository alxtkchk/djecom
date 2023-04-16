from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import *
from django.contrib.auth import authenticate, login


def index(request):
    items = Item.objects.all()
    return render(request, 'main/index.html', {'items': items})


def about(request):
    return render(request, 'main/about.html')


def signup(request):
    return render(request, 'registration/signup.html')


@csrf_protect
# def signin(request):
#     return render(request, 'registration/login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return ("You are not logged")

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'registration/logged_out.html')


def wishlist(request):
    return render(request, 'main/wishlist.html')


def checkout(request):
    return render(request, 'main/checkout.html')


def cart(request):
    return render(request, 'main/cart.html')
