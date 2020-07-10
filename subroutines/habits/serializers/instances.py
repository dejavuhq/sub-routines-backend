from django.utils import timezone

from rest_framework import serializers

from subroutines.habits.models import Instance
from subroutines.habits.serializers import HabitSerializer


class InstanceSerializer(serializers.ModelSerializer):
    """Instance serializer."""

    is_done = serializers.BooleanField()
    habit = HabitSerializer(read_only=True)

    class Meta:
        model = Instance
        fields = ["id", "habit", "date_to_do", "is_done"]

