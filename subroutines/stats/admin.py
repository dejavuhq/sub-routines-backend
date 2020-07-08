from django.contrib import admin

from subroutines.stats.models import Stat


@admin.register(Stat)
class StatsAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "date",
        "total_habits",
        "total_habits_today",
        "total_habits_done_today",
        "completion_rate",
        "completion_streak",
    ]

    readonly_fields = [
        "user",
        "date",
        "total_habits",
        "total_habits_today",
        "total_habits_done_today",
        "completion_rate",
        "completion_streak",
    ]

