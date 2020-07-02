from rest_framework import serializers
from subroutines.habits.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    """Habit model serializer."""
    name = serializers.CharField(required=True)
    recurrence = serializers.CharField(required=True)

    class Meta:

        model = Habit
        fields = ('id', 'name', 'description', 
            'recurrence', 'is_public',
            'is_completed', 'is_paused',
            'start_date', 'end_date'
        )