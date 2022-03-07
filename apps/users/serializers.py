from ast import keyword
from . models import User
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    """
    User serializer for SignUp/Register
    """
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name',)

