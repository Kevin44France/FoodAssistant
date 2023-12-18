import json
import requests

import apiUserLogin

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"number":"1"}

headers = apiUserLogin.headers

#response = {'recipes': [{'vegetarian': True, 'vegan': False, 'glutenFree': False, 'dairyFree': False, 'veryHealthy': False, 'cheap': False, 'veryPopular': False, 'sustainable': False, 'lowFodmap': False, 'weightWatcherSmartPoints': 112, 'gaps': 'no', 'preparationMinutes': -1, 'cookingMinutes': -1, 'aggregateLikes': 3, 'healthScore': 12, 'creditsText': 'Foodista.com – The Cooking Encyclopedia Everyone Can Edit', 'license': 'CC BY 3.0', 'sourceName': 'Foodista', 'pricePerServing': 569.65, 'extendedIngredients': [{'id': 1017, 'aisle': 'Cheese', 'image': 'cream-cheese.jpg', 'consistency': 'SOLID', 'name': 'cream cheese', 'nameClean': 'cream cheese', 'original': '16 ounces Cream cheese', 'originalName': 'Cream cheese', 'amount': 16.0, 'unit': 'ounces', 'meta': [], 'measures': {'us': {'amount': 16.0, 'unitShort': 'oz', 'unitLong': 'ounces'}, 'metric': {'amount': 453.592, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 1123, 'aisle': 'Milk, Eggs, Other Dairy', 'image': 'egg.png', 'consistency': 'SOLID', 'name': 'eggs', 'nameClean': 'egg', 'original': '2 Eggs', 'originalName': 'Eggs', 'amount': 2.0, 'unit': '', 'meta': [], 'measures': {'us': {'amount': 2.0, 'unitShort': '', 'unitLong': ''}, 'metric': {'amount': 2.0, 'unitShort': '', 'unitLong': ''}}}, {'id': 19335, 'aisle': 'Baking', 'image': 'sugar-in-bowl.png', 'consistency': 'SOLID', 'name': 'sugar', 'nameClean': 'sugar', 'original': '3/4 cup Sugar', 'originalName': 'Sugar', 'amount': 0.75, 'unit': 'cup', 'meta': [], 'measures': {'us': {'amount': 0.75, 'unitShort': 'cups', 'unitLong': 'cups'}, 'metric': {'amount': 150.0, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 1052050, 'aisle': 'Baking', 'image': 'vanilla.jpg', 'consistency': 'SOLID', 'name': 'vanilla', 'nameClean': 'vanilla', 'original': '1 teaspoon Vanilla', 'originalName': 'Vanilla', 'amount': 1.0, 'unit': 'teaspoon', 'meta': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'tsp', 'unitLong': 'teaspoon'}, 'metric': {'amount': 1.0, 'unitShort': 'tsp', 'unitLong': 'teaspoon'}}}, {'id': 18609, 'aisle': 'Sweet Snacks', 'image': 'vanilla-wafers.jpg', 'consistency': 'SOLID', 'name': 'vanilla wafers', 'nameClean': 'vanilla wafer cookies', 'original': 'Vanilla wafers', 'originalName': 'Vanilla wafers', 'amount': 1.0, 'unit': 'serving', 'meta': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'serving', 'unitLong': 'serving'}, 'metric': {'amount': 1.0, 'unitShort': 'serving', 'unitLong': 'serving'}}}], 'id': 651992, 'title': 'Miniature Cheesecakes', 'readyInMinutes': 45, 'servings': 1, 'sourceUrl': 'http://www.foodista.com/recipe/K34VXGS6/miniature-cheesecakes', 'image': 'https://spoonacular.com/recipeImages/651992-556x370.jpg', 'imageType': 'jpg', 'summary': 'If you have about <b>45 minutes</b> to spend in the kitchen, Miniature Cheesecakes might be a spectacular <b>lacto ovo vegetarian</b> recipe to try. This dessert has <b>2307 calories</b>, <b>39g of protein</b>, and <b>165g of fat</b> per serving. This recipe serves 1 and costs $5.7 per serving. It is brought to you by Foodista. Not a lot of people made this recipe, and 3 would say it hit the spot. Head to the store and pick up cream cheese, vanilla wafers, vanilla, and a few other things to make it today. Taking all factors into account, this recipe <b>earns a spoonacular score of 51%</b>, which is solid. Similar recipes are <a href="https://spoonacular.com/recipes/miniature-blueberry-cheesecakes-52208">Miniature Blueberry Cheesecakes</a>, <a href="https://spoonacular.com/recipes/miniature-cinnamon-roll-cheesecakes-544231">Miniature Cinnamon Roll Cheesecakes</a>, and <a href="https://spoonacular.com/recipes/miniature-peanut-butter-cheesecakes-423379">Miniature Peanut Butter Cheesecakes</a>.', 'cuisines': [], 'dishTypes': ['dessert'], 'diets': ['lacto ovo vegetarian'], 'occasions': [], 'instructions': '<ol><li>Cream cheese, sugar, eggs and vanilla together. Fill muffin pan with bake cups; place vanilla wafer at bottom of each. Fill half full of batter and bake 10 minutes or until set. Top with pie filling.</li></ol>', 'analyzedInstructions': [{'name': '', 'steps': [{'number': 1, 'step': 'Cream cheese, sugar, eggs and vanilla together. Fill muffin pan with bake cups; place vanilla wafer at bottom of each. Fill half full of batter and bake 10 minutes or until set. Top with pie filling.', 'ingredients': [{'id': 1017, 'name': 'cream cheese', 'localizedName': 'cream cheese', 'image': 'cream-cheese.jpg'}, {'id': 0, 'name': 'pie filling', 'localizedName': 'pie filling', 'image': ''}, {'id': 1052050, 'name': 'vanilla', 'localizedName': 'vanilla', 'image': 'vanilla.jpg'}, {'id': 19335, 'name': 'sugar', 'localizedName': 'sugar', 'image': 'sugar-in-bowl.png'}, {'id': 0, 'name': 'wafer', 'localizedName': 'wafer', 'image': 'shortbread-cookies.jpg'}, {'id': 1123, 'name': 'egg', 'localizedName': 'egg', 'image': 'egg.png'}], 'equipment': [{'id': 404671, 'name': 'muffin tray', 'localizedName': 'muffin tray', 'image': 'muffin-tray.jpg'}, {'id': 404784, 'name': 'oven', 'localizedName': 'oven', 'image': 'oven.jpg'}], 'length': {'number': 10, 'unit': 'minutes'}}]}], 'originalId': None, 'spoonacularScore': 16.824716567993164, 'spoonacularSourceUrl': 'https://spoonacular.com/miniature-cheesecakes-651992'}]}


def add_new_recipe(fichier_json):
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


for i in range(50):
	add_new_recipe("Data/dataset.json")

def nb_recipes(fichier_json):
	with open(fichier_json, "r", encoding='utf-8') as file:
		data = json.load(file)

	return print(len(data['recipes']))


nb_recipes("Data/dataset.json")
