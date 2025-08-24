from django.db import models
from recipe_manager.models import Recipe



class ShoppingList(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=125,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    recipes = models.ManyToManyField(
        Recipe,
        blank=True,
    )

    def __str__(self):
        return self.name
