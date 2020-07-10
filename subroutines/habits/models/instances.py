from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class InstanceManager(models.Manager):
    """Instance Manager."""

    def get_stats_per_habit_until_today(self, habit):
        """Returns the total of instances both done and don't per habit."""
        today = timezone.datetime.today()
        query = self.filter(habit=habit, date_to_do__lte=today)
        return {
            "total": query.count(),
            "total_done": query.filter(is_done=True).count(),
        }

    def get_stats_per_user(self, user):
        """
        Returns both the total of habit instances a user should have
        been done yesterday and total of instances done.
        """
        today = timezone.datetime.today() - timedelta(days=1)
        query = self.filter(user=user, date_to_do=yesterday)
        return {
            "total": query.count(),
            "total_done": query.filter(is_done=True).count(),
        }

    def get_for_today(self, user):
        """
        Returns a list of habit instances that a user must to do today
        excluding instances of habits paused.
        """
        today = timezone.datetime.today()
        return self.filter(user=user, date_to_do=today, habit__is_paused=False)


class Instance(models.Model):

    date_to_do = models.DateField(
        _("date"),
        default=timezone.now,
        help_text=_("Date at which an habit must be done"),
    )
    is_done = models.BooleanField(default=False)

    habit = models.ForeignKey("habits.Habit", on_delete=models.DO_NOTHING)
    user = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)

    objects = InstanceManager()

    def __str__(self):
        return self.habit.name

