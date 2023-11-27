from rest_framework import serializers


def validate_related_habit_and_reward(value):
    """Валидатор: Исключить одновременный выбор связанной привычки и указания вознаграждения."""
    if value.get('related_habit') and value.get('reward'):
        raise serializers.ValidationError("You can't choose both a related habit and a reward.")


def validate_time_to_complete_habit(value):
    """Валидатор: Время выполнения должно быть не больше 120 секунд."""
    if value.get('time_to_complete_habit') > 120:
        raise serializers.ValidationError("Time to complete habit should not exceed 120 seconds.")


def validate_pleasant_habit(value):
    """Валидатор: У приятной привычки не может быть вознаграждения или связанной привычки."""
    if value.get('is_pleasant_habit') and value.get('reward') or value.get('related_habit'):
        serializers.ValidationError("A pleasant habit should not have a reward or a related habit.")


def validate_periodicity(value):
    """Валидатор: Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""
    if value.get('periodicity') not in ['daily', 'weekly']:
        serializers.ValidationError("The minimum periodicity is once in 7 days for non-daily habits.")
