from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    is_pharmacist = models.BooleanField(default=False)
    is_delivery_person = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Pharmacist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="pending")
    legal_document = models.ImageField(upload_to='legal_docs/', null=True, blank=True)

    def __str__(self):
        return self.user.first_name


class DeliveryPerson(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="pending")

    def __str__(self):
        return self.user.first_name


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    pharmacy_manager = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    CATEGORIES = [
        ("medicine", "medicine"),
        ("device", "device"),
        ("nutritional", "nutritional"),
    ]
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    discount = models.IntegerField()
    price = models.IntegerField()
    unit = models.CharField(max_length=100)
    quantity = models.IntegerField()
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    ratings = models.IntegerField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage_instructions = models.TextField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_STATUSES = [
        ("pending", "pending"),
        ("accepted", "accepted"),
        ("rejected", "rejected")
    ]
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField()
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100, choices=ORDER_STATUSES)
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    status = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Payment(models.Model):
    PAYMENT_METHODS = [
        ("cash", "cash"),
        ("credit_card", "credit_card"),
        ("debit_card", "debit_card"),
        ("mobile_money", "mobile_money")
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHODS)
    amount = models.IntegerField()
    payment_date = models.DateField()

    def __str__(self):
        return self.name


class Review(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Message(models.Model):
    sender_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    message_date = models.DateField()

    def __str__(self):
        return self.message
