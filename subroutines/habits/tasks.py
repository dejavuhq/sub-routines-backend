from datetime import timedelta

from django.db.models import Exists, OuterRef
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


@celery_app.task()
def update_habit_instances():
    """
    Task to update number of habit instances for a week.
    """
    tomorrow = timezone.datetime.today() + timedelta(days=1)
    queryset = Instance.objects.filter(habit=OuterRef("pk"), date_to_do__gte=tomorrow)
    active_habits = Habit.objects.filter(
        ~Exists(queryset), is_paused=False, is_completed=False
    )

    for habit in active_habits:

        start_date = tomorrow
        end_date = start_date + timedelta(days=6)

        if habit.end_date and end_date > habit.end_date:
            end_date = habit.end_date

        occurrences = habit.recurrence.occurrences(
            dtstart=timezone.datetime(
                start_date.year, start_date.month, start_date.day
            ),
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


@celery_app.task()
def update_habit_stats(habit_pk):
    """
    Task to update habit stats each time a habit instance is updated.
    """
    # Habit stats
    today = timezone.datetime.today()
    habit = Habit.objects.get(pk=habit_pk)
    habit_stats = Instance.objects.get_stats_per_habit(habit=habit, date=today)

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


@celery_app.task()
def update_habits_stats():
    """
    Task to update stats for a list of habits.
    """
    yesterday = timezone.datetime.today() - timedelta(days=1)
    habits = Habit.objects.filter(
        is_paused=False, is_completed=False, instance__date_to_do=yesterday
    )

    for habit in habits:
        habit_stats = Instance.objects.get_stats_per_habit(habit=habit, date=yesterday)

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
