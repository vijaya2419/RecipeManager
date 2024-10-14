# recipe_manager.py

import json
from typing import Dict, List

# Define the recipe data structure
Recipe = Dict[str, List[str]]
Recipes = Dict[str, Recipe]

"""
 Function to Load recipes from file
"""


def load_recipes() -> Recipes:
    try:
        with open("data/recipes.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


"""
 Function to save recipes to file.
 input :  recipe details
 output: success / failure message
"""


def save_recipes(recipes: Recipes) -> None:
    with open("recipes.json", "w") as file:
        json.dump(recipes, file)


"""
 Function to add a new recipe.
 input :  recipe details
 output: success / failure message
"""


def add_recipe(recipes: Recipes) -> None:
    title = input("Enter recipe title: ")
    ingredients = []
    print("Enter ingredients (leave blank to finish):")
    while True:
        ingredient = input("> ")
        if not ingredient:
            break
        ingredients.append(ingredient)
    instructions = []
    print("Enter instructions (leave blank to finish):")
    while True:
        instruction = input("> ")
        if not instruction:
            break
        instructions.append(instruction)
    recipes[title] = {"ingredients": ingredients, "instructions": instructions}
    save_recipes(recipes)
    print(f"Recipe '{title}' added successfully!")


"""
 Function to view all recipes.
 input :  N/A
 output: Full recipe list
"""


def view_recipes(recipes: Recipes) -> None:
    if not recipes:
        print("No recipes found.")
        return
    print("Available recipes:")
    for title, recipe in recipes.items():
        print(f"- {title}")


"""
 Function to search for a recipe.
 input : title of the recipe
 output: recipe list
"""


def search_recipes(recipes: Recipes) -> None:
    query = input("Enter search query: ")
    matches = [
        (title, recipe)
        for title, recipe in recipes.items()
        if query.lower() in title.lower()
        or any(query.lower() in ingredient.lower() for ingredient in recipe["ingredients"])
    ]
    if not matches:
        print(f"No recipes found for '{query}'.")
        return
    print(f"Recipes matching '{query}':")
    for title, recipe in matches:
        print(f"- {title}")


"""
 Function to edit an existing recipe.
 input : title of the recipe
 output: success message if modified successfully 
"""


# Edit a recipe
def edit_recipe(recipes: Recipes) -> None:
    title = input("Enter recipe title: ")
    if title not in recipes:
        print(f"Recipe '{title}' not found.")
        return
    recipe = recipes[title]
    print(f"Editing recipe '{title}':")
    ingredients = recipe["ingredients"]
    print("Current ingredients:")
    for i, ingredient in enumerate(ingredients, start=1):
        print(f"{i}. {ingredient}")
    print("Enter new ingredients (leave blank to finish):")
    new_ingredients = []
    while True:
        ingredient = input("> ")
        if not ingredient:
            break
        new_ingredients.append(ingredient)
    recipe["ingredients"] = new_ingredients or ingredients
    instructions = recipe["instructions"]
    print("Current instructions:")
    for i, instruction in enumerate(instructions, start=1):
        print(f"{i}. {instruction}")
    print("Enter new instructions (leave blank to finish):")
    new_instructions = []
    while True:
        instruction = input("> ")
        if not instruction:
            break
        new_instructions.append(instruction)
    recipe["instructions"] = new_instructions or instructions
    save_recipes(recipes)
    print(f"Recipe '{title}' updated successfully!")


"""
 Function to delete a recipe.
 input : title of the recipe
 output: success if deleted 
"""


#
def delete_recipe(recipes: Recipes) -> None:
    title = input("Enter recipe title: ")
    if title not in recipes:
        print(f"Recipe '{title}' not found.")
        return
    del recipes[title]
    save_recipes(recipes)
    print(f"Recipe '{title}' deleted successfully!")


"""
 Main function to display main menu for recipe manager.
 Need to choose one of the option from the list.
 
"""


# Main program loop
def main() -> None:
    recipes = load_recipes()
    while True:
        print("\nRecipe Manager")
        print("1. Add recipe")
        print("2. View recipes")
        print("3. Search recipes")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            view_recipes(recipes)
        elif choice == "3":
            search_recipes(recipes)
        elif choice == "4":
            edit_recipe(recipes)
        elif choice == "5":
            delete_recipe(recipes)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


# default main function
if __name__ == "__main__":
    main()
