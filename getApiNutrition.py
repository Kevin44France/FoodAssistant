import json
import requests

import apiUserLogin


def list_id(fichier_json):
	with open(fichier_json, "r", encoding='utf-8') as file:
		data = json.load(file)

	id_list = []
	for recipe in data['recipes']:
		id_list.append(recipe['id'])

	return id_list

def add_new_recipe_nutrition(fichier_json, headers, id_recipe):
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + str(id_recipe) + "/nutritionWidget.json"
	response = requests.get(url, headers=headers).json()

	with open(fichier_json, "r", encoding='utf-8') as file:
		data = json.load(file)

	recipe = {"id": id_recipe, "nutrition": []}
	recipe['nutrition'].append(response)
	data['recipes'].append(recipe)

	with open(fichier_json, "w", encoding='utf-8') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


dataset_path = "Data/dataset.json"
dataset_nutrition_path = "Data/dataset_nutrition.json"
list_recipes_id = list_id(dataset_path)

def add_recipe(header):
	list_recipes_nutritions_id = list_id(dataset_nutrition_path)
	id_recipe = list_recipes_id[0]
	i = 0

	while id_recipe in list_recipes_nutritions_id and i < len(list_recipes_id):
		id_recipe = list_recipes_id[i]
		i += 1
	print(id_recipe)

	if len(list_recipes_nutritions_id) != len(list_recipes_id):
		add_new_recipe_nutrition(dataset_nutrition_path, header, id_recipe)
	else:
		print("Toutes les recettes ont déjà leur nutrition")
	print(len(list_recipes_nutritions_id)+1)


for j in range(50):
	add_recipe(apiUserLogin.headersBaptiste)
	add_recipe(apiUserLogin.headersKevin)
	add_recipe(apiUserLogin.headersMaxime)
