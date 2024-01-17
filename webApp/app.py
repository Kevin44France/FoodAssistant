import json

from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

find = "recipes/findByIngredients"
randomFind = "recipes/random"


def find_recipe_by_id(recipe_id):
    with open('../Data/dataset.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for recipe in data['recipes']:
            if recipe['id'] == recipe_id:
                return recipe
    return None  # Retourne None si aucune recette n'est trouvée


def meets_dietary_requirements(recipe, restrictions):
    # Check each recipe against the dietary restrictions
    return all(recipe.get(restriction, False) for restriction in restrictions)


def determine_age_group(age):
    if age <= 8:
        return "4-8"
    elif age <= 13:
        return "9-13"
    elif age <= 18:
        return "14-18"
    elif age <= 30:
        return "19-30"
    elif age <= 50:
        return "31-50"
    else:
        return "51+"


@app.route('/')
@app.route('/page/<int:page>')
def search_page(page=1):
    per_page = 18  # Nombre de recettes par page
    with open('../Data/user_profile.json', 'r') as user_file:
        user_profile = json.load(user_file)
    dietary_restrictions = user_profile['dietaryRestrictions']

    with open('../Data/dataset.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Filtrer les recettes en fonction des restrictions alimentaires
    filtered_recipes = [recipe for recipe in data['recipes'] if
                        meets_dietary_requirements(recipe, dietary_restrictions)]

    # Pagination
    total_recipes = len(filtered_recipes)
    total_pages = -(-total_recipes // per_page)  # Calcul du nombre total de pages
    paginated_recipes = filtered_recipes[(page-1)*per_page : page*per_page]

    return render_template('search.html', recipes=paginated_recipes, page=page, total_pages=total_pages)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    # Load the recipes data
    with open('../Data/dataset.json', 'r', encoding='utf-8') as file:  # Change the file path if necessary
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
            return render_template('recipes.html', recipe=recipe, nutrition=nutrition_info['nutrition'][
                0])  # Assuming you want the first item in nutrition info
        else:
            # Recipe is found but no nutrition info is found for this recipe
            return render_template('recipes.html', recipe=recipe, nutrition=None)
    else:
        # Recipe ID not found
        return "Recipe not found", 404


@app.route('/user', methods=['GET', 'POST'])
def user_profile():
    user_data_path = '../Data/user_profile.json'
    nutrition_data_path = '../Data/daily_nutrition.json'
    dataset_path = '../Data/dataset.json'  # Assurez-vous que ce chemin est correct

    if request.method == 'POST':
        # Si l'utilisateur soumet un ingrédient à ajouter
        if 'ingredient_name' in request.form:
            with open(user_data_path, 'r+') as file:
                user_data = json.load(file)
                if 'ingredients' not in user_data:
                    user_data['ingredients'] = []
                user_data['ingredients'].append({
                    'name': request.form['ingredient_name'],
                    'amount': float(request.form['ingredient_amount']),
                    'unit': request.form['ingredient_unit']
                })
                file.seek(0)
                json.dump(user_data, file, indent=4)
                file.truncate()
            return redirect(url_for('user_profile'))
        # Si l'utilisateur met à jour ses informations de profil
        else:
            user_data = {
                'firstName': request.form.get('firstName'),
                'lastName': request.form.get('lastName'),
                'sex': request.form.get('sex'),
                'age': request.form.get('age'),
                'dietaryRestrictions': request.form.getlist('dietaryRestrictions'),
                # Vous pouvez ajouter ici les autres éléments comme les calories, etc.
            }
            with open(user_data_path, 'w') as file:
                json.dump(user_data, file, indent=4)
            return redirect(url_for('user_profile'))

    else:
        with open(nutrition_data_path, 'r', encoding='utf-8') as file:
            nutrition_data = json.load(file)

        with open(dataset_path, 'r', encoding='utf-8') as file:
            dataset = json.load(file)
            ingredient_units = {}

            # Pour chaque recette dans le jeu de données, on s'assure également que l'ingrédient n'est pas vide
            # et que les ingrédiens sont uniques

            for recipe in dataset['recipes']:
                for ingredient in recipe['extendedIngredients']:
                    ingredient_name = ingredient.get('nameClean')
                    ingredient_unit = ingredient['measures']['metric']['unitShort']
                    if ingredient_name:
                        if ingredient_name not in ingredient_units:
                            ingredient_units[ingredient_name] = {'unit': ingredient_unit, 'count': 1}
                        else:
                            if ingredient_units[ingredient_name]['unit'] == ingredient_unit:
                                ingredient_units[ingredient_name]['count'] += 1
                            else:
                                if ingredient_units[ingredient_name]['count'] < 2:
                                    ingredient_units[ingredient_name] = {'unit': ingredient_unit, 'count': 1}

        ingredients_list = sorted(ingredient_units.keys())

        final_ingredient_units = {ingredient: unit_info['unit'] for ingredient, unit_info in ingredient_units.items()}

        try:
            with open(user_data_path, 'r', encoding='utf-8') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}

        age_group = determine_age_group(int(user_data.get('age', 0)))

        return render_template(
            'user.html',
            user_data=user_data,
            nutrition_data=nutrition_data,
            age_group=age_group,
            ingredients=ingredients_list,
            ingredient_units=final_ingredient_units)


@app.route('/update_calories', methods=['POST'])
def update_calories():
    try:
        # Load the current user profile data
        with open('../Data/user_profile.json', 'r') as file:
            user_profile = json.load(file)

        # Get the change in calories from the AJAX request
        change = request.json.get('change', 0)

        # Update the calories value, ensuring it stays within 0-100%
        user_profile['calories'] = max(0, min(100, user_profile.get('calories', 50) + change))

        # Save the updated profile
        with open('../Data/user_profile.json', 'w') as file:
            json.dump(user_profile, file)

        return jsonify(success=True, new_calories=user_profile['calories'])

    except Exception as e:
        return jsonify(success=False, error=str(e))


def update_nutrition(user_data, nutrient, change):
    user_data[nutrient] = max(user_data.get(nutrient, 0) + change, 0)


def reset_nutrition(user_data):
    for nutrient in ['calories', 'proteins', 'fats', 'carbs', 'calcium', 'iron', 'magnesium', 'potassium', 'zinc', 'vitamin A', 'vitamin E', 'vitamin C']:
        user_data[nutrient] = 0


@app.route('/update_nutrition', methods=['POST'])
def update_nutrition_route():
    user_data_path = '../Data/user_profile.json'
    nutrient = request.form['nutrient']
    change = int(request.form['change'])

    try:
        with open(user_data_path, 'r') as file:
            user_data = json.load(file)

        update_nutrition(user_data, nutrient, change)

        with open(user_data_path, 'w') as file:
            json.dump(user_data, file, indent=4)

        return redirect(url_for('user_profile'))
    except Exception as e:
        return str(e), 500


@app.route('/reset_nutrition', methods=['POST'])
def reset_nutrition_route():
    user_data_path = '../Data/user_profile.json'

    try:
        with open(user_data_path, 'r') as file:
            user_data = json.load(file)

        reset_nutrition(user_data)

        with open(user_data_path, 'w') as file:
            json.dump(user_data, file, indent=4)

        return redirect(url_for('user_profile'))
    except Exception as e:
        return str(e), 500


@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    user_data_path = '../Data/user_profile.json'

    # Obtenez les données du formulaire
    ingredient_name = request.form['ingredient_name']
    ingredient_amount = float(request.form['ingredient_amount'])
    ingredient_unit = request.form['ingredient_unit']

    # Chargez les données utilisateur existantes
    with open(user_data_path, 'r+') as file:
        user_data = json.load(file)

        # Ajoutez le nouvel ingrédient
        if 'ingredients' not in user_data:
            user_data['ingredients'] = []
        user_data['ingredients'].append({
            'name': ingredient_name,
            'amount': ingredient_amount,
            'unit': ingredient_unit
        })

        # Rembobinez le fichier et écrivez les données mises à jour
        file.seek(0)
        json.dump(user_data, file, indent=4)
        file.truncate()  # Supprimez le reste du fichier si les nouvelles données sont plus courtes

    return redirect(url_for('user_profile'))

@app.route('/clear_ingredients', methods=['POST'])
def clear_ingredients():
    # Chemin vers le fichier JSON
    json_file_path = '../Data/user_profile.json'

    # Lire le fichier JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Vider la liste des ingrédients
    if 'ingredients' in data:
        data['ingredients'] = []

    # Réécrire le fichier JSON mis à jour
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return redirect(url_for('user_profile'))

if __name__ == '__main__':
    app.run()
