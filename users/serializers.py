from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
           Сериализатор для модели пользователя.

           Attributes:
               id (int): Уникальный идентификатор пользователя.
               email (str): Адрес электронной почты пользователя.
               first_name (str): Имя пользователя.
               last_name (str): Фамилия пользователя.
    """

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name']


class UserLoginSerializer(serializers.Serializer):
    """Сериализатор для аутентификации пользователя
        Attributes:
            email (str): Адрес электронной почты пользователя.
            password (str): Пароль пользователя.
        Methods:
            validate(data): Проверяет переданные данные на наличие
                корректных учетных данных пользователя.
        Raises:
            serializers.ValidationError: Если учетные данные некорректны или отсутствуют.
        Return:
            data (dict):  Словарь с проверенными данными, включая объект пользователя (если успешно).
    """
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='autorization')

        data['user'] = user

        return data
