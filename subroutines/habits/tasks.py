from datetime import timedelta

from django.utils import timezone

from config import celery_app
from subroutines.users.models import User
from subroutines.habits.models import Habit, Instance


@celery_app.task(max_retries=3)
def create_habit_instances(habit_pk):
    """
    Each time a habit is created this task is called
    to create instances.
    """
    # Obtain created habit.
    habit = Habit.objects.get(pk=habit_pk)

    start_date = habit.start_date
    end_date = start_date + timedelta(days=6)

    if habit.end_date and end_date > habit.end_date:
        end_date = habit.end_date

    occurrences = habit.recurrence.occurrences(
        dtstart=timezone.datetime(start_date.year, start_date.month, start_date.day),
        dtend=timezone.datetime(end_date.year, end_date.month, end_date.day),
    )

    # By each occurrence found create a new instance.
    for occurrence in occurrences:
        Instance.objects.create(
            date_to_do=occurrence,
            habit=habit,
            user=User.objects.get(pk=habit.user_id),
            is_done=False,
        )

