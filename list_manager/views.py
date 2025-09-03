from django.shortcuts import render, redirect
from .models import ShoppingList
from recipe_manager.models import Recipe, Ingredient
from app.settings import NOT_FOUND_VIEW



def view_shopping_lists(request):
    try:
        shopping_lists = ShoppingList.objects.all()
    except:
        shopping_lists = None

    context = {
        "page_title": "Shopping Lists",
        "shopping_lists": shopping_lists,
    }

    return render(request, "shopping_lists.html", context)


def view_shopping_list(request, id):
    try:
        shopping_list = ShoppingList.objects.get(id=id)
    except ShoppingList.DoesNotExist:
        return redirect(NOT_FOUND_VIEW)
    
    shopping_list_ingredients = Ingredient.objects.filter(shopping_list=shopping_list)

    for recipe in shopping_list.recipes.all():
        try:
            recipe_ingredients = Ingredient.objects.filter(recipe=recipe)
        except:
            recipe_ingredients = None
        
        if recipe_ingredients != None:
            shopping_list_ingredients |= recipe_ingredients
    
    context = {
        "page_title": "Shopping List",
        "shopping_list": shopping_list,
        "shopping_list_ingredients": shopping_list_ingredients,
        "recipes": shopping_list.recipes.all(),
    }

    return render(request, "shopping_list.html", context)
