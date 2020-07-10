from django.utils import timezone

from recurrence import fields

from rest_framework import serializers
from subroutines.habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Habit model serializer."""

    name = serializers.CharField(required=True)
    recurrence = fields.RecurrenceField()

    class Meta:

        model = Habit
        fields = (
            "id",
            "name",
            "description",
            "recurrence",
            "is_public",
            "is_completed",
            "is_paused",
            "start_date",
            "end_date",
            "total_instances",
            "total_instances_done",
            "completion_rate",
        )

