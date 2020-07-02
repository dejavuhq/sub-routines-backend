from django.db import models

from subroutines.utils.models import SubRoutinesModel

class Habit(SubRoutinesModel):
    """
    Habit model for subroutines app. Extend from django abstract model
    to define extra fields needed to logic bussiness.
    """
    name = models.CharField('name', max_length=50)
    description = models.CharField('description', max_length=200)
    completed = models.BooleanField(default=False)
    paused = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    recurrence = models.CharField('recurrence', max_length=200)

    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)