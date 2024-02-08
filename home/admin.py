from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

admin.site.register(DeliveryPerson)
admin.site.register(Pharmacy)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Message)
admin.site.register(Cart)
admin.site.register(CartItem)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "first_name", "last_name", "address",
                    "phone_number", "is_pharmacist", "is_delivery_person", "is_staff", "is_active")
    search_fields = ("username", "first_name", "last_name",
                     "address", "phone_number")
    list_editable = ("is_staff", "is_pharmacist",
                     "is_delivery_person", "is_active")


@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ("user", "status")
    list_editable = ("status",)
