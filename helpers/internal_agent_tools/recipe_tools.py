from strands import tool
from recipe_manager.models import Recipe
from app.settings import HTTP_PROTOCOL, SITE_URL



@tool
def get_recipes():
    """Gets all available recipes
    - Use the 'link' as an html element
    """
    recipe_data = {}
    recipes = list(Recipe.objects.all().values("name", "directions", "id"))
    button_class = "inline-flex items-center justify-center rounded-full border border-slate-300 bg-white px-6 py-3 text-sm font-semibold text-slate-700 shadow-sm transition-colors hover:border-slate-400 hover:bg-slate-50 hover:text-slate-900 focus-visible:ring-4 focus-visible:ring-slate-200 focus-visible:outline-none"
    for recipe in recipes:
        name = recipe["name"]
        id = recipe["id"]
        recipe_data[name] = {
            "directions": recipe["directions"],
            "link": f"<a class='{button_class}' href='{HTTP_PROTOCOL}{SITE_URL}/recipe/{id}'>view recipe here</a>"
        }

    return recipe_data
