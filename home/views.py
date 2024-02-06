from django.shortcuts import render
from .models import *


def home(request):
    return render(request, "pages/index.html")


def login(request):
    return render(request, "pages/auth/login.html")


def signup(request):
    return render(request, "pages/auth/signup.html")


def products(request):
    context = {
        "medicines" : Medicine.objects.all(),
    }
    print(context["medicines"][0])
    return render(request, "pages/products.html", context)


def cart(request):
    return render(request, "pages/cart.html")
