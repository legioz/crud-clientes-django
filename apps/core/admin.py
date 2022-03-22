from django.contrib import admin
from apps.core import models

admin.site.site_header = "CRUD Administration"
admin.site.site_title = "CRUD Portal Admin"
admin.site.index_title = "Welcome to CRUD Portal"


@admin.register(models.User)
class RoutineAdmin(admin.ModelAdmin):
    filter_horizontal = ["groups", "user_permissions"]
    list_display = [
        "email",
        "first_name",
        "birth",
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    search_fields = ["email", "first_name", "last_name"]
    list_filter = ["is_active", "is_active", "is_deleted"]
    per_page = 20
