from django.urls import path, include
from rest_framework import routers
from django.views.generic import TemplateView
from . import views

router = routers.DefaultRouter()
router.register('short_link', views.LinkViewSet,
                basename='link')
router.register('my_links', views.MyLinksViewSet,
                basename='my_links')         

urlpatterns = [
    path('home/', include(router.urls)),
    path('', TemplateView.as_view(template_name='short/index.html')),
    path('<str:pk>/', views.LinkRedirect.as_view(), name = 'new_url'),
]