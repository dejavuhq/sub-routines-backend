"""Profile model."""

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Utilities
from subroutines.utils.models import SubRoutinesModel


class Profile(SubRoutinesModel):
    """Profile model.
    This model is for the creation of the User-profile.
    In the first instance it is his biography and his image.
    """

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    picture = models.ImageField(
        "profile picture", upload_to="users/pictures/", blank=True, null=True
    )
    biography = models.TextField(max_length=500, null=True)
    is_public = models.BooleanField(
        default=True, help_text=_("Public profiles show all information about users.")
    )

    def __str__(self):
        """Return users str"""
        return str(self.user)
