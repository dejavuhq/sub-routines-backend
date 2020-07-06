from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from recurrence import fields

from subroutines.utils.models import SubRoutinesModel


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

    user = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)

