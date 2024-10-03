from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import MovieViewSet, ActionViewSet

router = SimpleRouter()
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'action', ActionViewSet, basename='action')

urlpatterns = [
    path('', include(router.urls)),
]