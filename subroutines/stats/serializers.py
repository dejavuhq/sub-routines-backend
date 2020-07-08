from django.contrib.auth import get_user_model

from rest_framework import serializers
from subroutines.stats.models import Stat

User = get_user_model()

class StatSerializer(serializers.ModelSerializer):
    """Serializer model serializer."""
    
    class Meta:
        model = Stat
        fields = [
            "date",
            "total_habits",
            "total_habits_today",
            "total_habits_done_today",
            "completion_rate",
            "completion_streak",
            "user",
        ]
