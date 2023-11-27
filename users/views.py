from django.contrib.auth import login
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users.serializers import UserLoginSerializer, UserSerializer, UserRegistrationSerializer


class UserLoginViewSet(viewsets.ViewSet):
    """
    Представление (ViewSet) для аутентификации пользователя и создания токена.
    Attributes:
        serializer_class (UserLoginSerializer): Класс сериализатора для аутентификации.

    Methods:
        create(request, *args, **kwargs): Метод для обработки запроса на аутентификацию пользователя,
             создания токена и возврата данных пользователя вместе с токеном.

    Returns:
        Response: Ответ, содержащий токен и данные пользователя.
    """
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(request_body=UserLoginSerializer)
    def create(self, request, *args, **kwargs):
        # Создается экземпляр сериализатора (UserLoginSerializer) с переданными данными запроса и контекстом запроса.
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # Извлекается объект пользователя из валидированных данных сериализатора.
        user = serializer.validated_data['user']

        # Аутентификация пользователя в системе
        login(request, user)

        # Получается или создается токен для пользователя с использованием модели токена DRF (Token)
        token, created = Token.objects.get_or_create(user=user)

        user_serializer = UserSerializer(user)

        return Response({'token': token.key, 'user': user_serializer.data}, status=status.HTTP_200_OK)


class UserRegistrationViewSet(viewsets.ViewSet):
    """
    Представление (ViewSet) для регистрации нового пользователя.

    Attributes:
        serializer_class (UserRegistrationSerializer): Класс сериализатора для регистрации.

    Methods:
        create(request, args, **kwargs): Метод для обработки запроса на создание нового пользователя.

    Returns:
        Response: Ответ с данными нового пользователя.
    """

    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
