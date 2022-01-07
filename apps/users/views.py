from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from . serializers import UserSerializer
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from backend.utils.mailer import SendResetPasswordMail
from django.urls import reverse
from django.template.loader import render_to_string

from django.conf import settings as conf_settings


class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(status=status.HTTP_403_FORBIDDEN)


class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email = reset_password_token.user.email
    username = reset_password_token.user.username
    url = f"{conf_settings.CLIENT_URL}/reset-password?t={reset_password_token.key}"
    
    context = {
        'email': email,
        'username': username,
        'url': url
    }

    print(f"\n\nInfo enviada: \n - email: {email}\n - user: {username}\n - url: {url}\n\n")

    SendResetPasswordMail(email, context, username=username).send_email()