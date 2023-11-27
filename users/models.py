from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
            Расширенная модель пользователя для проекта Django.

            Заменяет стандартную модель пользователя Django для включения
            дополнительной информации, такой как id пользователя в телеграм.

            Attributes:
                email (str): Уникальный адрес электронной почты пользователя.
                chat_id(str): id чата в tg
        """
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта пользователя')
    chat_id = models.CharField(max_length=20, unique=True, verbose_name='id пользователя в телеграм')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
