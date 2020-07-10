from django.contrib.auth import get_user_model

from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from subroutines.habits.models import Habit, Instance
from subroutines.habits.serializers import HabitSerializer, InstanceSerializer
from subroutines.habits.tasks import create_habit_instances


class HabitViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    serializer_class = HabitSerializer
    lookup_field = "id"

    def get_permissions(self):
        """Assign permissions based on actions."""
        if self.action in ["list", "update", "partial_update"]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Restrict list to user authenticated."""
        user = self.request.user
        return Habit.objects.filter(user=user)

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)
        create_habit_instances.apply_async([habit.pk], countdown=10)
