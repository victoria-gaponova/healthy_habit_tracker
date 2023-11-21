from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Серилиализатор для модели Habit"""
    class Meta:
        model = Habit
        fields = '__all__'