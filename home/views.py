from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect


def home(request):
    context = {"four_medicines": Medicine.objects.all()[:4]}
    return render(request, "pages/index.html", context)


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

        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        return redirect('login')

    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'pages/auth/signup.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        featured = request.POST.get('featured')
        image = request.FILES.get('image')

        medicine = Medicine(
            name=name,
            description=description,
            price=price,
            category=category,
            featured=featured,
            image=image
        )
        medicine.save()
        return redirect('products')

    return render(request, 'pages/create_product.html')


def products(request):
    context = {
        "all_medicines": Medicine.objects.all(),
        "category_medicine": Medicine.objects.filter(category="medicine"),
        "category_device": Medicine.objects.filter(category="device"),
        "category_nutritional": Medicine.objects.filter(category="nutritional"),
        "featured": Medicine.objects.filter(featured=True),
    }
    return render(request, "pages/products.html", context)


def medicine(request, id):
    context = {"medicine": Medicine.objects.get(id=id)}
    return render(request, "pages/medicine.html", context)


def add_to_cart(request, id):
    medicine = Medicine.objects.get(id=id)
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_item = CartItem.objects.get_or_create(medicine=medicine, cart=cart)[0]
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    context = {
        "cart": cart,
        "cart_items": cart_items}
    return render(request, "pages/cart.html", context)


def checkout(request):
    return render(request, "pages/checkout.html")
