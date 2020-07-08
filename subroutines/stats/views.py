from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from subroutines.stats.serializers import StatSerializer
from subroutines.stats.models import Stat

User = get_user_model()

class StatViewSet(ListModelMixin, GenericViewSet):
    serializer_class = StatSerializer
    queryset = Stat.objects.all()

    def get_permissions(self):
        """Assign permissions based on actions."""
        if self.action in ["retrieve", "list"]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
    
    def get_queryset(self):
        """ List user statistics """
        user = self.request.user
        return Stat.objects.filter(user=user)
