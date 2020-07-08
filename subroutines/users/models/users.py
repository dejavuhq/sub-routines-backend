from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from subroutines.utils.models import SubRoutinesModel


class UserManager(BaseUserManager):
    """Extends user manager to add helper functions."""

    def get_users_with_instances(self):
        """Returns just users with habit instances to do today."""
        today = timezone.datetime.today()
        return self.filter(instance__date_to_do=today)


class User(SubRoutinesModel, AbstractUser):
    """
    User model for subroutines app. Extend from django abstract model
    to define extra fields needed to logic bussiness.
    """

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": "A user with that email already exists"},
    )
    picture = models.ImageField(
        "profile picture", upload_to="users/pictures/", blank=True, null=True
    )
    biography = models.TextField(max_length=500, null=True)
    is_public = models.BooleanField(
        default=True, help_text=_("Public profiles show all information about users.")
    )
    is_verified = models.BooleanField(
        _("verified"),
        default=False,
        help_text=_(
            "Determine if an user has a verified account. "
            "Set to true when user verified its email address."
        ),
    )

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        """Return username"""
        return self.username
