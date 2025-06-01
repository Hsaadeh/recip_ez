from django.shortcuts import render
from recipe_manager.models import Recipe


def view_recipes(request):
    try:
        recipes = Recipe.objects.all()
    except:
        recipes = None

    context = {
        "page_title": "Recipes",
        "recipes": recipes
    }

    return render(request, "recipes.html", context)


def view_add_recipe(request):
    try:
        recipes = Recipe.objects.all()
    except:
        recipes = None

    context = {
        "page_title": "Add Recipe",
        "recipes": recipes
    }

    return render(request, "add_recipe.html", context)

