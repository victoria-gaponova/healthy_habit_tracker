from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitListCreateAPIView(generics.CreateAPIView):
    """Представление для создания  и просмотра список привычек пользователя
        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов привычек в JSON.
    """
    serializer_class = HabitSerializer

    def get_queryset(self):
        """
        Метод для получения cписка привычек текущего пользователя
        Returns: Возращает привычки текущего пользователя
        """
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Метод для автоматического сохранения пользователя, создающего привычку.

        """
        serializer.save(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """Представлениe для просмотра списка публичных привычек
        Attributes:
            queryset (QuerySet): Набор объектов привычек.
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов привычек в JSON.
            """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer


class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления привычки
        Attributes:
            queryset (QuerySet): Набор объектов привычек.
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов привычек в JSON.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        """
        Метод для получения привычки текущего пользователя
        Returns: возвращает привычки текущего пользователя
        """
        return Habit.objects.filter(user=self.request.user)

