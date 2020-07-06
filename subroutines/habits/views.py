from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from subroutines.users.serializers import (
    UserSerializer,
    UserSignUpSerializer,
    UserLoginSerializer,
)
from subroutines.habits.serializers import HabitSerializer

from subroutines.habits.models import Habit

User = get_user_model()


class HabitViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
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
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Restrict list to user authenticated."""
        user = self.request.user
        return Habit.objects.filter(user=user)

    def habit_detail(self, request, pk):
        user = self.request.user
        queryset = Habit.objects.filter(user=user, pk=pk)
        serializer = HabitSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
