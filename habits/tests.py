from django.test import TestCase
from rest_framework import serializers
from django.utils import timezone

from users.models import User
from .models import Habit
from .validators import (
    validate_related_habit_and_reward,
    validate_time_to_complete_habit,
    validate_pleasant_habit,
    validate_periodicity,
)


class HabitModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(
            email="testuser@example.com", chat_id="testchatid"
        )

    def test_habit_model(self):
        # Create a habit instance
        habit = Habit.objects.create(
            user=self.user,
            place="Test Place",
            time=timezone.now().time(),
            action="Test Action",
            is_pleasant_habit=True,
            periodicity="daily",
            time_to_complete_habit=60,
            is_public=True,
        )

        # Test the __repr__ method
        self.assertEqual(
            habit.__repr__(),
            f"Habit(Test Place, {habit.time}, Test Action, True, None, daily, True)",
        )

        # Test the __str__ method
        self.assertEqual(
            str(habit), f"Я буду {habit.action} в {habit.time} в {habit.place}"
        )

    def test_validators(self):
        # Test validate_related_habit_and_reward
        with self.assertRaises(serializers.ValidationError):
            validate_related_habit_and_reward(
                {"related_habit": 1, "reward": "Test Reward"}
            )

        # Test validate_time_to_complete_habit
        with self.assertRaises(serializers.ValidationError):
            validate_time_to_complete_habit({"time_to_complete_habit": 150})

        # Test validate_pleasant_habit
        with self.assertRaises(serializers.ValidationError):
            validate_pleasant_habit(
                {"is_pleasant_habit": True, "reward": "Test Reward"}
            )

        # Test validate_periodicity
        with self.assertRaises(serializers.ValidationError):
            validate_periodicity({"periodicity": "monthly"})
