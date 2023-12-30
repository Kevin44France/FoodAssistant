import json

from flask import Flask, render_template, request

import requests

app = Flask(__name__)

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "5ffebd22e0msh81794727dc35776p116ef2jsn0264b6e23bd5",
}

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
    recipe = find_recipe_by_id(recipe_id)
    if recipe:
        return render_template('recipes.html', recipe=recipe)
    else:
        # Gérer le cas où la recette n'est pas trouvée
        return "Recette non trouvée", 404


@app.route('/user')
def user_profile():
    return render_template('user.html')


if __name__ == '__main__':
    app.run()
