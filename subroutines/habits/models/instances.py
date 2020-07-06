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

    def get_stats_per_user_for_today(self, user):
        """
        Returns both the total of habit instances a user should have
        be done today and total of instances done.
        """
        today = timezone.datetime.today()
        query = self.filter(user=user, date_to_do=today)
        return {
            "total": query.count(),
            "total_done": query.filter(is_done=True).count(),
        }

    def get_for_today(self):
        """Returns a list of habit instances to do today."""
        today = timezone.datetime.today()
        return self.filter(date_to_do=today)


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

