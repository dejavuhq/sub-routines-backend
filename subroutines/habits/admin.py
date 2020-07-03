from django.contrib import admin

from subroutines.habits.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_completed",
        "start_date",
        "end_date",
        "is_paused",
        "is_public",
        "recurrence",
    ]

    search_fields = ["name", "is_completed"]

