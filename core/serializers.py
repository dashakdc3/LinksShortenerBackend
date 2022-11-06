from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        id = serializers.UUIDField(read_only=True)
        fields = ['username', 'password', 'email' ]

class UserSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
