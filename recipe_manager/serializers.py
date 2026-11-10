from rest_framework import serializers
from recipe_manager import models


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = [
            "id",
            "owner",
            "name",
            "description",
            "directions",
            "recipe_type",
            "image",
        ]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = '__all__'
