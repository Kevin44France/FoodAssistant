import json

from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

find = "recipes/findByIngredients"
randomFind = "recipes/random"


def find_recipe_by_id(recipe_id):
    with open('../Data/dataset.json', 'r') as file:
        data = json.load(file)
        for recipe in data['recipes']:
            if recipe['id'] == recipe_id:
                return recipe
    return None  # Retourne None si aucune recette n'est trouvée


@app.route('/')
def search_page():
    with open('../Data/dataset.json', 'r') as file:
        data = json.load(file)
    return render_template('search.html', recipes=data['recipes'])


@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    # Load the recipes data
    with open('../Data/dataset.json', 'r') as file:  # Change the file path if necessary
        recipes_data = json.load(file)

    # Load the nutrition data
    with open('../Data/dataset_nutrition.json', 'r') as file:  # Change the file path if necessary
        nutrition_data = json.load(file)

    # Find the recipe by ID
    recipe = next((item for item in recipes_data['recipes'] if item['id'] == recipe_id), None)

    if recipe:
        # Find the nutrition information for the recipe by ID
        nutrition_info = next((item for item in nutrition_data['recipes'] if item['id'] == recipe_id), None)

        if nutrition_info:
            # Pass both recipe and nutrition information to the template
            return render_template('recipes.html', recipe=recipe, nutrition=nutrition_info['nutrition'][0])  # Assuming you want the first item in nutrition info
        else:
            # Recipe is found but no nutrition info is found for this recipe
            return render_template('recipes.html', recipe=recipe, nutrition=None)
    else:
        # Recipe ID not found
        return "Recipe not found", 404




@app.route('/user', methods=['GET', 'POST'])
def user_profile():
    user_data_path = '../Data/user_profile.json'  # Le chemin vers votre fichier JSON

    if request.method == 'POST':
        # Recueillir les données du formulaire
        user_data = {
            'firstName': request.form.get('firstName'),
            'lastName': request.form.get('lastName'),
            'height': request.form.get('height'),
            'age': request.form.get('age'),
            'dietaryRestrictions': request.form.getlist('dietaryRestrictions')  # Cela recueille toutes les restrictions cochées
        }

        # Écrire les données dans le fichier JSON
        with open(user_data_path, 'w') as file:
            json.dump(user_data, file, indent=4)

        return redirect(url_for('user_profile'))

    else:
        # Lire les données existantes
        try:
            with open(user_data_path, 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Si le fichier n'existe pas ou est vide
            user_data = {}

        return render_template('user.html', user_data=user_data)


if __name__ == '__main__':
    app.run()
