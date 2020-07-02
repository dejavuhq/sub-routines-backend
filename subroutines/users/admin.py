from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from subroutines.users.models import Profile, User


User = get_user_model()


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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin"""

    list_display = ["biography"]
    search_fields = [
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    ]


admin.site.register(User, UserAdmin)
