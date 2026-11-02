from django.shortcuts import render
from recipe_manager.models import Recipe, Ingredient, RECIPE_TYPE_CHOICES
from django.contrib.auth.decorators import login_required


@login_required(login_url="/sign-in")
def view_recipes(request):
    recipe_data = []

    try:
        recipes = Recipe.objects.all()
    except:
        recipes = None
    
    if recipes != None:
        for recipe in recipes:
            try:
                ingredient_count = Ingredient.objects.filter(recipe=recipe).count()
            except:
                ingredient_count = None
            
            recipe_data_item = {
                "recipe": recipe,
                "ingredient_count": ingredient_count
            }

            recipe_data.append(recipe_data_item)

    context = {
        "page_title": "Recipes",
        "recipe_data": recipe_data
    }

    return render(request, "recipes.html", context)


@login_required(login_url="/sign-in")
def view_recipe(request, id):
    try:
        recipe = Recipe.objects.get(id=id)
    except:
        recipe = None

    try:
        ingredients = Ingredient.objects.filter(recipe=recipe)
    except:
        ingredients = None

    context = {
        "page_title": "Recipe",
        "recipe": recipe,
        "ingredients": ingredients,
    }

    return render(request, "recipe.html", context)


@login_required(login_url="/sign-in")
def view_add_recipe(request):
    try:
        recipes = Recipe.objects.all()
    except:
        recipes = None

    context = {
        "page_title": "Add Recipe",
        "recipes": recipes,
        "recipe_type_choices": RECIPE_TYPE_CHOICES,
    }

    return render(request, "add_recipe.html", context)

