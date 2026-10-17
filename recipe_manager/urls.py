from django.urls import path
from rest_framework.routers import DefaultRouter

from . import api
from . import views


view_urls = [
    path("recipes/", views.view_recipes, name="view_recipes"),
    path("recipe/<str:id>", views.view_recipe, name="view_recipe"),
    path("add-recipe/", views.view_add_recipe, name="view_add_recipe"),
]

api_urls = []

router = DefaultRouter()

router.register(r"api/v1/recipes", api.RecipeViewSet, basename="recipes")
router.register(r"api/v1/ingredients", api.IngredientViewSet, basename="ingredients")

urlpatterns = view_urls + api_urls + router.urls
