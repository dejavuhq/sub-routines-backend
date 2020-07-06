from django.db import models
from django.utils import timezone

from subroutines.users.models import User
from subroutines.utils.models import SubRoutinesModel


class Stat(SubRoutinesModel):
    """User stats model."""

    # Day of calculus
    date = models.DateField(default=timezone.now)
    total_habits = models.PositiveIntegerField(default=0)
    total_habits_today = models.PositiveIntegerField(default=0)
    total_habits_done_today = models.PositiveIntegerField(default=0)
    completion_rate = models.PositiveIntegerField(default=0)
    completion_streak = models.PositiveIntegerField(default=0)

    user = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)

    def update_stats(self):
        if self.completion_rate == 1:
            self.completion_streak += 1
        else:
            self.completion_streak = self.completion_streak

        self.save(update_fields=["completion_streak"])
