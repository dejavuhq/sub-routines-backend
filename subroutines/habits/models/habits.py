from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from recurrence import fields

from subroutines.utils.models import SubRoutinesModel


class HabitManager(models.Manager):
    """Habit Manager with utilities to create stats"""

    def get_total_active_habits_for_user(self, user):
        """Returns the total of no paused habits for a user."""
        return self.filter(is_paused=False).count()

    def get_active_habits_for_user(self, user):
        """Returns a list of all active habits for a user."""
        return self.filter(user=user, is_paused=False)


class Habit(SubRoutinesModel):
    """
    Habit model for subroutines app. Extend from django abstract model
    to define extra fields needed to logic bussiness.
    """

    name = models.CharField(_("name"), max_length=50)
    description = models.CharField(_("description"), max_length=200)
    start_date = models.DateField(_("start date"), default=timezone.now)
    end_date = models.DateField(_("end date"), blank=True, null=True)
    is_completed = models.BooleanField(_("completed"), default=False)
    is_paused = models.BooleanField(_("paused"), default=False)
    is_public = models.BooleanField(_("public"), default=False)
    recurrence = fields.RecurrenceField()

    # Habit stats
    total_instances = models.PositiveIntegerField(default=0)
    total_instances_done = models.PositiveIntegerField(default=0)
    completion_rate = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    user = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)

    # Uses a custom manager
    objects = HabitManager()

    def __str__(self):
        return self.name

