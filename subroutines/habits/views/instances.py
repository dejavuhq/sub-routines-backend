from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from subroutines.habits.models import Habit, Instance
from subroutines.habits.serializers import InstanceSerializer
from subroutines.habits.tasks import update_habit_stats


class InstanceViewSet(
    mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    serializer_class = InstanceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Instance.objects.get_for_today(user=user)

    def perform_update(self, serializer):
        instance = serializer.save()
        update_habit_stats.apply_async([instance.habit.id], countdown=10)

