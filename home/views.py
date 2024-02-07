from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect


def home(request):
    return render(request, "pages/index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'pages/auth/login.html', {'error_message': error_message})

    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'pages/auth/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone_number=phone_number,
            password=password
        )
        user.save()
        return redirect('login')

    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'pages/auth/signup.html')


def logout(request):
    auth_logout(request)
    return redirect('login')
    

def products(request):
    context = {
        "all_medicines": Medicine.objects.all(),
        "category_medicine": Medicine.objects.filter(category="medicine"),
        "category_device": Medicine.objects.filter(category="device"),
        "category_nutritional": Medicine.objects.filter(category="nutritional"),
        "featured": Medicine.objects.filter(featured=True),
    }
    return render(request, "pages/products.html", context)


def cart(request):
    return render(request, "pages/cart.html")


def checkout(request):
    return render(request, "pages/checkout.html")
