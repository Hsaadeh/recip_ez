from django.db import models
# from moneyfield import MoneyField


class Recipe(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    name = models.CharField(
        max_length=125,
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
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
    # unit_cost = MoneyField(
    #     decimal_places=2,
    #     max_digits=8
    # )

    def __str__(self):
        return self.name
