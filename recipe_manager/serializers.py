from rest_framework import serializers
from recipe_manager import models


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Ingredient
