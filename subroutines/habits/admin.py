from django.contrib import admin

from subroutines.habits.models import Habit, Instance


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
        "completion_rate",
    ]

    search_fields = ["name", "is_completed"]


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ["date_to_do", "is_done", "habit", "user"]
    ordering = ["date_to_do"]
