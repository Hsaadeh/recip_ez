from strands import tool
from recipe_manager.models import Recipe


@tool(context=True)
def get_recipes():
    """Gets all available recipes"""
    recipes = list(Recipe.objects.all().values_list())
    return recipes
