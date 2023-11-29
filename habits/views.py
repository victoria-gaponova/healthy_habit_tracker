from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListCreateAPIView(generics.CreateAPIView):
    """Представление для создания  и просмотра список привычек пользователя
    Attributes:
        serializer_class (HabitSerializer): Сериализатор, используемый для преобразования объектов привычек в JSON.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        """
        Метод для получения cписка привычек текущего пользователя
        Returns: Возращает привычки текущего пользователя
        """
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Метод для автоматического сохранения пользователя, создающего привычку."""
        serializer.save(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """Представлениe для просмотра списка публичных привычек
    Attributes:
        queryset (QuerySet): Набор объектов привычек.
        serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов привычек в JSON.
    """

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination


class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления привычки
    Attributes:
        queryset (QuerySet): Набор объектов привычек.
        serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов привычек в JSON.
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Метод для получения привычки текущего пользователя
        Returns: возвращает привычки текущего пользователя
        """
        return Habit.objects.filter(user=self.request.user)
