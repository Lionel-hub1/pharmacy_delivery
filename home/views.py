from django.shortcuts import render


def home(request):
    return render(request, "pages/index.html")


def login(request):
    return render(request, "pages/auth/login.html")


def signup(request):
    return render(request, "pages/auth/signup.html")


def products(request):
    return render(request, "pages/products.html")
