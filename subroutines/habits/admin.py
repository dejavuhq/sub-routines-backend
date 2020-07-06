from django.contrib import admin

from subroutines.habits.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "start_date",
        "end_date",
        "recurrence",
        "is_completed",
        "is_paused",
        "is_public",
    ]

    search_fields = ["name", "is_completed"]

