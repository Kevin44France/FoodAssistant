import json
import requests

import apiUserLogin

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"number":"1"}



def add_new_recipe(fichier_json, headers):
	response = requests.get(url, headers=headers, params=querystring).json()

	with open(fichier_json, "r", encoding='utf-8') as file:
		data = json.load(file)

	new_recipe = response['recipes'][0]
	new_recipe_id = new_recipe['id']

	if new_recipe_id is not None and any(recipe.get('id') == new_recipe_id for recipe in data['recipes']):
		print(f"Une recette avec l'ID {new_recipe_id} est déjà présente dans le dataset.")
		return

	data['recipes'].append(new_recipe)

	with open(fichier_json, "w", encoding='utf-8') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


dataset_path = "Data/dataset.json"
for i in range(50):
	add_new_recipe(dataset_path, apiUserLogin.headersBaptiste)
	add_new_recipe(dataset_path, apiUserLogin.headersKevin)
	add_new_recipe(dataset_path, apiUserLogin.headersMaxime)

def nb_recipes(fichier_json):
	with open(fichier_json, "r", encoding='utf-8') as file:
		data = json.load(file)

	return print(len(data['recipes']))


nb_recipes("Data/dataset.json")
