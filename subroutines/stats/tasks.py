from django.contrib.auth import get_user_model


from config import celery_app
from subroutines.habits.models import Habit, Instance
from subroutines.stats.models import Stat


User = get_user_model()


@celery_app.task()
def update_user_stats():
    """Task to update user stats daily"""

    # User stats
    users = User.objects.get_users_with_instances()

    for user in users:
        # Get total habit instances today and total habit instances done today
        user_stats = Instance.objects.get_stats_per_user_for_today(user=user)
        # Completion rate total done / total
        completion_rate = user_stats["total_done"] / user_stats["total"]

        # create stats
        stat = Stat.objects.create(
            total_habits=Habit.objects.get_total_active_habits_for_user(user=user),
            total_habits_today=user_stats["total"],
            total_habits_done_today=user_stats["total_done"],
            completion_rate=completion_rate,
            user=user,
        )

        # update completion streak according completion rate
        # 100% of completion rate is +1 in streak for the user.
        stat.update_stats()

