from django.contrib import admin
from apps.customer import models


@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "number",
    ]
    search_fields = ["user__email", "user__first_name", "user__last_name"]
    per_page = 20


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "address",
    ]
    search_fields = ["user__email", "user__first_name", "user__last_name"]
    per_page = 20
