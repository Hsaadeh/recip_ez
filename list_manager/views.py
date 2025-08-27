from django.shortcuts import render
from .models import ShoppingList
from recipe_manager.models import Recipe, Ingredient



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
    combined_ingredients = []

    try:
        shopping_list = ShoppingList.objects.get(id=id)
    except:
        shopping_list = None
    
    try:
        shopping_list_ingredients = Ingredient.objects.filter(shopping_list=shopping_list)
    except:
        shopping_list_ingredients = None

    for recipe in shopping_list.recipes.all():
        try:
            recipe_ingredients = Ingredient.objects.filter(recipe=recipe)
        except:
            recipe_ingredients = None
        
        if recipe_ingredients != None:
            shopping_list_ingredients |= recipe_ingredients
    
    print(shopping_list_ingredients)
    
    context = {
        "page_title": "Shopping List",
        "shopping_list": shopping_list,
        "shopping_list_ingredients": shopping_list_ingredients,
        "recipes": shopping_list.recipes.all(),
    }

    return render(request, "shopping_list.html", context)
