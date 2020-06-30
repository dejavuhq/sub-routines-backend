from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from subroutines.utils.models import SubRoutinesModel


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

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    is_verified = models.BooleanField(
        _("verified"),
        default=False,
        help_text=_("Determine if an user has a verified account. "
                    "Set to true when user verified its email address." 
        )
    )

    def __str__(self):
        """Return username"""
        return self.username
