from django.db import models

from users.models import User


class Habit(models.Model):
    """
        Модель, представляющая собой привычку пользователя.

        Поля:
        - user (ForeignKey): Пользователь, создавший привычку.
        - place (CharField): Место, в котором необходимо выполнять привычку.
        - time (TimeField): Время, когда необходимо выполнять привычку.
        - action (CharField): Действие, которое представляет из себя привычку.
        - is_pleasant_habit (BooleanField): Признак приятной привычки.
        - related_habit (ForeignKey): Связанная привычка, если таковая имеется.
        - periodicity (CharField): Периодичность выполнения привычки для напоминания в днях.
        - reward (CharField): Вознаграждение за выполнение привычки.
        - time_to_complete_habit (IntegerField): Время, которое предположительно потратит пользователь на выполнение привычки.
        - is_public (BooleanField): Признак публичности привычки.
        """
    PERIODICITY_CHOICES = [
        ('daily', 'Ежедневная'),
        ('weekly', 'Еженедельная'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=300, help_text='место, в котором необходимо выполнять привычку')
    time = models.TimeField(auto_now=False, auto_now_add=False, help_text='время, когда необходимо выполнять привычку')
    action = models.CharField(max_length=300, help_text='действие, которое представляет из себя привычка')
    is_pleasant_habit = models.BooleanField(default=False, help_text='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                      help_text='связанная привычка,если таковая имеется')
    periodicity = models.CharField(max_length=20, choices=PERIODICITY_CHOICES, default='daily',
                                   help_text='периодичность выполнения привычки для напоминания в днях')
    reward = models.CharField(max_length=300, help_text='вознаграждение для пользователя за выполнение привычки')
    time_to_complete_habit = models.IntegerField(
        help_text='время, которое предположительно потратит пользователь на выполнение привычки')
    is_public = models.BooleanField(default=False, help_text='признак публичности привычки')
