from django.db import models
from django.utils.translation import ugettext_lazy as _


class SubRoutinesModel(models.Model):
    """
    SubRoutines base model.
    This model act as abstract model and define fields that all others
    models in the application must to have.
    """

    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("Date time at which an object was created")
    )
    updated_at = models.DateTimeField(
        _("updated_at"),
        auto_now=True,
        help_text=_("Date time at which an object was modified")
    )

    class Meta:
        abstract = True
        
        get_latest_by = "created_at"
        ordering = ["-created_at", "-updated_at"]