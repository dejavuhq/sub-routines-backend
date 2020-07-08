from django.db.models import F

from config import celery_app
from subroutines.habits.models import Habit, Instance


@celery_app.task()
def update_habit_stats():
    active_habits = Habit.objects.filter(is_paused=False)

    for habit in active_habits:
        habit_stats = Instance.objects.get_stats_per_habit_until_today(habit=habit)

        try:
            completion_rate = habit_stats["total_done"] / habit_stats["total"]
        except ZeroDivisionError:
            completion_rate = 0

        habit.total_instances = habit_stats["total"]
        habit.total_instances_done = habit_stats["total_done"]
        habit.completion_rate = completion_rate

        habit.save(
            update_fields=["total_instances", "total_instances_done", "completion_rate"]
        )

