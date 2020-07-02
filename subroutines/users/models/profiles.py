"""Profile model."""

from django.db import models

# Utilities
from subroutines.utils.models import SubRoutinesModel

class Profile(SubRoutinesModel):
    """Profile model.
    This model is for the creation of the User-profile.
    In the first instance it is his biography and his image.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """Return users str"""
        return str(self.user)
