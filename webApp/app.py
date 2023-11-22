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


@app.route('/')
def search_page():
    return render_template('search.html')


@app.route('/recipes')
def get_recipes():
    if str(request.args['ingridients']).strip() != "":
        # If there is a list of ingridients -> list
        querystring = {"number": "5", "ranking": "1", "ignorePantry": "false",
                       "ingredients": request.args['ingridients']}
        response = requests.request("GET", url + find, headers=headers, params=querystring).json()
        return render_template('recipes.html', recipes=response)
    else:
        # Random recipes
        querystring = {"number": "5"}
        response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
        print(response)
        return render_template('recipes.html', recipes=response['recipes'])


@app.route('/recipe')
def get_recipe():
    recipe_id = request.args['id']
    recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)
    ingedientsWidget = "recipes/{0}/ingredientWidget.json".format(recipe_id)
    equipmentWidget = "recipes/{0}/equipmentWidget.json".format(recipe_id)

    recipe_info = requests.request("GET", url + recipe_info_endpoint, headers=headers).json()

    recipe_headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "5ffebd22e0msh81794727dc35776p116ef2jsn0264b6e23bd5",
        'accept': "application/json"
    }
    querystring = {"defaultCss": "true", "showBacklink": "false"}

    recipe_info['inregdientsWidget'] = requests.request("GET", url + ingedientsWidget, headers=recipe_headers,
                                                        params=querystring).text
    recipe_info['equipmentWidget'] = requests.request("GET", url + equipmentWidget, headers=recipe_headers,
                                                      params=querystring).text
    print("Ingredient Widget URL:", url + ingedientsWidget)
    print("Ingredient Widget Headers:", recipe_headers)
    print("Ingredient Widget Querystring:", querystring)

    # Make the request
    ingredient_widget_response = requests.request("GET", url + ingedientsWidget, headers=recipe_headers,
                                                  params=querystring)
    print("Ingredient Widget Response:", ingredient_widget_response.text)

    return render_template('recipe.html', recipe=recipe_info)


if __name__ == '__main__':
    app.run()
