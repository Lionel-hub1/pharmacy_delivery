from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        featured = request.POST.get('featured')
        quantity = request.POST.get('quantity')
        pharmacy = request.POST.get('pharmacy')
        image = request.FILES.get('image')

        medicine = Medicine(
            name=name,
            description=description,
            price=price,
            category=category,
            featured=featured,
            quantity=quantity,
            pharmacy_id=pharmacy,
            image=image
        )
        medicine.save()
        print("Saved successfullyyyyyy")
        return redirect('products')

    context = {"pharmacies": Pharmacy.objects.all()}
    return render(request, 'pages/create_product.html', context)


@login_required(login_url='login')
def update_product(request, id):
    if request.method == 'PUT':
        try:
            try:
                medicine = Medicine.objects.get(id=id)
                medicine.name = request.POST.get('name')
                medicine.description = request.POST.get('description')
                medicine.price = request.POST.get('price')
                medicine.category = request.POST.get('category')
                medicine.featured = request.POST.get('featured')
                medicine.quantity = request.POST.get('quantity')
                medicine.pharmacy = request.POST.get('pharmacy')
                medicine.image = request.FILES.get('image')
                medicine.save()
                print("Medicine updated successfully")
            except Medicine.DoesNotExist:
                print("Medicine does not exist")
        except Medicine.DoesNotExist:
            print("Medicine does not exist")
        return redirect('products')

    context = {
        "medicine": Medicine.objects.get(id=id),
        "pharmacies": Pharmacy.objects.all()
    }
    return render(request, 'pages/update_product.html', context)


@login_required(login_url='login')
def create_pharmacy(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        pharmacy = Pharmacy(
            name=name,
            address=address,
            phone_number=phone_number
        )
        pharmacy.save()
        return redirect('products')

    return render(request, 'pages/create_pharmacy.html')


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
    try:
        medicine = Medicine.objects.get(id=id)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(medicine=medicine, cart=cart)
    except CartItem.DoesNotExist:
        cart_item = None

    context = {
        "medicine": medicine,
        "cart_item": cart_item
    }
    return render(request, "pages/medicine.html", context)


@login_required(login_url='login')
def add_to_cart(request, id):
    if request.method == 'POST':
        medicine = Medicine.objects.get(id=id)
        cart = Cart.objects.get_or_create(user=request.user)[0]
        cart_item = CartItem.objects.get_or_create(
            medicine=medicine, cart=cart)[0]
        cart_item.quantity = request.POST.get('quantity')
        cart_item.save()
        return redirect('cart')
    else:
        return redirect('products')


def remove_from_cart(request, id):
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(medicine_id=id, cart=cart)
    cart_item.delete()
    messages.success(request, 'Item successfully deleted from cart.')
    return redirect('cart')


@login_required(login_url='login')
def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_amount = 0
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        total_amount += item.medicine.price * item.quantity
    context = {
        "cart": cart,
        "cart_items": cart_items,
    }
    return render(request, "pages/cart.html", context)


def checkout(request):
    return render(request, "pages/checkout.html")
