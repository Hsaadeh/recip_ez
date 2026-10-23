from strands import tool



@tool
def abilities():
    """Explains what the assistant is able to do when asked by the user."""
    
    abilities = f"""I am able to:
    \n- Create Recipes
    \n- Create Shopping Lists
    \n- Find Recipes based on preferences
    \n- etc...
    """

    return abilities
