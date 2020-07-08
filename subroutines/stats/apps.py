from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StatsConfig(AppConfig):
    name = "subroutines.stats"
    verbose_name = _("Stats")

