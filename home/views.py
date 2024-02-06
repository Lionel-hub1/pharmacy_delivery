from django.shortcuts import render
from rest_framework.views import APIView


def home(request):
    return render(request, "pages/index.html")


def login(request):
    return render(request, "pages/auth/login.html")


def signup(request):
    return render(request, "pages/auth/signup.html")


def products(request):
    return render(request, "pages/products.html")


def cart(request):
    return render(request, "pages/cart.html")
