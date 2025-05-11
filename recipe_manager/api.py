from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from recipe_manager import models
from .serializers import RecipeSerializer


# @permission_classes([IsAuthenticated])
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer
