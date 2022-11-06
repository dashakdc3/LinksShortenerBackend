from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, UserCreateSerializer
from .models import User

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer