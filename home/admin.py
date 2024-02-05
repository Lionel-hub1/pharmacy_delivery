from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "first_name", "last_name", "address", "phone_number", "is_pharmacist", "is_delivery_person")
    search_fields = ("username", "first_name", "last_name", "address", "phone_number")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "address", "phone_number", "password1", "password2"),
            },
        ),
    )
    ordering = ("username",)
