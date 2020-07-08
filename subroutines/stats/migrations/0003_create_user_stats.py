from django.conf import settings
from django.db import migrations

from django_celery_beat.models import CrontabSchedule, PeriodicTask


def create_periodic_task(apps, schema_editor):

    # Create schedule to run periodic task daily at 00:30
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="5",
        hour="0",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
        timezone=settings.TIME_ZONE,
    )

    # Create periodic task
    PeriodicTask.objects.create(
        crontab=schedule,
        name="Create user stats",
        task="subroutines.stats.tasks.create_user_stats",
    )


class Migration(migrations.Migration):

    dependencies = [("stats", "0002_stat_user")]

    operations = [migrations.RunPython(create_periodic_task)]
