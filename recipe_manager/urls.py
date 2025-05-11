from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import RecipeViewSet


view_urls = [
]

api_urls = [
]

router = DefaultRouter()

router.register(r"api/v1/recipes", RecipeViewSet, basename="recipes")

urlpatterns = view_urls + api_urls + router.urls
