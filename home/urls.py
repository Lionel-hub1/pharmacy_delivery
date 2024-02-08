from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("create_product/", views.create_product, name="create_product"),
    path("create_pharmacy/", views.create_pharmacy, name="create_pharmacy"),
    path("update_product/<int:id>/", views.update_product, name="update_product"),
    path("products/", views.products, name="products"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("logout/", views.logout, name="logout"),
    path("medicine/<int:id>/", views.medicine, name="medicine"),
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<int:id>/", views.remove_from_cart, name="remove_from_cart"),
]
