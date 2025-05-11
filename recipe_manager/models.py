from django.db import models


class Recipe(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    name = models.CharField(
        max_length=125,
    )

    def __str__(self):
        return self.name
