from django.conf import settings
from django.db import migrations

from django_celery_beat.models import CrontabSchedule, PeriodicTask


def create_periodic_task(apps, schema_editor):

    # Create schedule to run periodic task daily at 00:30
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="5",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
        timezone=settings.TIME_ZONE,
    )

    # Create periodic task
    PeriodicTask.objects.create(
        crontab=schedule,
        name="Update habit instances",
        task="subroutines.habits.tasks.update_habit_instances",
    )


class Migration(migrations.Migration):

    dependencies = [("habits", "0001_initial")]

    operations = [migrations.RunPython(create_periodic_task)]
