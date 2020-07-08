from django.contrib.auth import get_user_model

from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from subroutines.habits.models import Habit
from subroutines.habits.serializers import HabitSerializer
from subroutines.habits.tasks import create_habit_instances

User = get_user_model()


class HabitViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        """Assign permissions based on actions."""
        if self.action in ["list", "update", "partial_update"]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)
        create_habit_instances.apply_async([habit.pk], countdown=10)

    def get_queryset(self):
        """Restrict list to user authenticated."""
        user = self.request.user
        return Habit.objects.filter(user=user)

    def habit_detail(self, request, pk):
        user = self.request.user
        queryset = Habit.objects.filter(user=user, pk=pk)
        serializer = HabitSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
