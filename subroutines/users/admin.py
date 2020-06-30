from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        ("User", {"fields": ("is_verified",)}),
    ) + auth_admin.UserAdmin.fieldsets
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_verified",
        "is_active",
        "is_superuser",
    ]
    search_fields = ["username", "email"]
