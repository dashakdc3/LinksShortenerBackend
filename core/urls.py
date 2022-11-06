from django.urls import path
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.generic import TemplateView
urlpatterns = [
    path('user/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterView.as_view(), name='auth_register'),
]
