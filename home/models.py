from django.db import models


# class User(models.Model):
#     TYPES_OF_USERS = [
#         ("admin", "admin"),
#         ("pharmacist", "pharmacist"),
#         ("customer", "customer"),
#         ("delivery_person", "delivery_person")
#     ]
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     address = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=100)
#     user_type = models.CharField(max_length=100, choices=TYPES_OF_USERS)

#     def __str__(self):
#         return self.name


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    pharmacist = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    CATEGORIES = [
        ("antibiotic", "antibiotic"),
        ("antiseptic", "antiseptic"),
        ("analgesic", "analgesic"),
        ("antipyretic", "antipyretic"),
        ("antifungal", "antifungal")
    ]
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    form = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Prescription(models.Model):
#     image = models.ImageField(upload_to='images/', null=True, blank=True)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     dosage_instructions = models.TextField()
#     quantity = models.IntegerField()
#     status = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class Order(models.Model):
    ORDER_STATUSES = [
        ("pending", "pending"),
        ("accepted", "accepted"),
        ("rejected", "rejected")
    ]
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
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
    # delivery_person = models.ForeignKey(User, on_delete=models.CASCADE)
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


# class Review(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     review = models.TextField()
#     rating = models.IntegerField()

#     def __str__(self):
#         return self.name


# class Message(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     message_date = models.DateField()

#     def __str__(self):
#         return self.name
