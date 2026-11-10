import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from recipe_manager.models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer


# @permission_classes([IsAuthenticated])
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_recipe(request):
    """Api endpoint to create a recipe"""
    request_data = request.data
    updated_data = request_data.copy()
    updated_data["owner"] = request.user.id
    recipe = RecipeSerializer(data=updated_data)
    
    if recipe.is_valid():
        new_recipe = recipe.save()
    else:
        data = {
            "message": "Bad request, invalid data",
            "error": recipe.errors
        }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    data = {
        "message": "Recipe added",
        "new_recipe_id": new_recipe.id
    }
    return Response(data=data, status=status.HTTP_200_OK)
