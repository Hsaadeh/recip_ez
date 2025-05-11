from rest_framework import serializers
from recipe_manager import models


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
        )
        model = models.Recipe
