from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import viewsets

from dateutil.relativedelta import relativedelta

from subroutines.stats.serializers import StatSerializer
from subroutines.stats.models import Stat


class StatViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        """
        Limit queryset to user logged in.
        Just retrieve stats greater than or equal to a year before.
        """
        user = self.request.user
        return Stat.objects.filter(
            user=user, date__gte=timezone.localdate() - relativedelta(year=1)
        )
