from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    validate_related_habit_and_reward,
    validate_time_to_complete_habit,
    validate_pleasant_habit,
    validate_periodicity,
)


class HabitSerializer(serializers.ModelSerializer):
    """Серилиализатор для модели Habit"""

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        """Валидаторы для модели Habit."""
        validate_related_habit_and_reward(data)
        validate_time_to_complete_habit(data)
        validate_pleasant_habit(data)
        validate_periodicity(data)
        return data
