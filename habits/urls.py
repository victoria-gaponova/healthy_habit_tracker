from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListCreateAPIView, PublicHabitListAPIView, HabitDetailAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListCreateAPIView.as_view(), name='habits-list-create'),
    path('habits/public/', PublicHabitListAPIView.as_view(), name='habits_public-list'),
    path('<int:pk>/habit/', HabitDetailAPIView.as_view(), name='habit_detail'),
]