from django.db import models
from djmoney.models.fields import MoneyField
from profiles.models import CustomUser


RECIPE_TYPE_CHOICES = (
    ("Breakfast", "Breakfast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
    ("Snack", "Snack"),
)


class Recipe(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=125,
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    directions = models.TextField(
        blank=True,
        null=True
    )
    recipe_type = models.CharField(
        choices=RECIPE_TYPE_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    shopping_list = models.ForeignKey(
        "list_manager.ShoppingList",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=125,
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=4,
    )
    unit = models.CharField(
        max_length=50,
    )
    unit_cost = MoneyField(
        default=0.00,
        max_digits=14, 
        decimal_places=2, 
        default_currency='USD'
    )

    def __str__(self):
        return self.name
