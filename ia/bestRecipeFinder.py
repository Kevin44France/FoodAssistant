from pycsp3 import *
import json

def charger_recettes(chemin_fichier_json):
    with open(chemin_fichier_json, 'r') as file:
        data = json.load(file)
        recettes = []
        for recette in data["recipes"]:
            id_recette = recette["id"]
            nutrition = recette["nutrition"][0]  # Supposons que le premier élément contient les données nutritionnelles
            calories = int(round(float(nutrition["calories"].replace("kcal", "").strip())))
            proteines = int(round(float(nutrition["protein"].replace("g", "").strip())))
            glucides = int(round(float(nutrition["carbs"].replace("g", "").strip())))
            recettes.append((id_recette, calories, proteines, glucides))

        return recettes

def charger_nutrition_recettes(chemin_fichier_json):
    with open(chemin_fichier_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
        nutrition_recettes = {}
        for recette in data["recipes"]:
            id_recette = recette["id"]
            nutrition = recette["nutrition"][0]  # Ajustez si nécessaire
            calories = int(round(float(nutrition["calories"].replace("kcal", "").strip())))
            proteines = int(round(float(nutrition["protein"].replace("g", "").strip())))
            glucides = int(round(float(nutrition["carbs"].replace("g", "").strip())))
            nutrition_recettes[id_recette] = (calories, proteines, glucides)
        return nutrition_recettes

def charger_ingredients_recettes(chemin_fichier_json):
    with open(chemin_fichier_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
        ingredients_recettes = {}
        for recette in data["recipes"]:
            id_recette = recette["id"]
            ingredients = [ingredient["nameClean"] for ingredient in recette["extendedIngredients"]]
            ingredients_recettes[id_recette] = ingredients
        return ingredients_recettes

def charger_profil_utilisateur(chemin_fichier_json):
    with open(chemin_fichier_json, 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == '__main__':
    recettes = charger_recettes('../Data/dataset_nutrition.json')

    choix_recettes = VarArray(size=len(recettes), dom=range(2))

    # Appliquer une contrainte pour chaque recette

    satisfy(
        recettes[i][1] * choix_recettes[i] <= 1000 for i in range(len(recettes)) # Calories définies par défaut
    )
    # satisfy(
    #     recettes[i][2] * choix_recettes[i] <= 50 for i in range(len(recettes)) # Protéines définies par défaut
    # )
    # satisfy(
    #     recettes[i][3] * choix_recettes[i] <= 50 for i in range(len(recettes)) # Glucides définies par défaut
    # )

    """
    # Charger les données pour prendre en compte les ingrédients et les profils utilisateurs
    
    profil_utilisateur = charger_profil_utilisateur('../Data/user_profile.json')
    nutrition_recettes = charger_nutrition_recettes('../Data/dataset_nutrition.json')
    ingredients_recettes = charger_ingredients_recettes('../Data/dataset.json')

    ingredients_utilisateur = set(ingredient['name'] for ingredient in profil_utilisateur['ingredients'])
    choix_recettes = VarArray(size=len(nutrition_recettes), dom=range(2))

    for id_recette in nutrition_recettes:
        if id_recette in ingredients_recettes:
            calories, proteines, glucides = nutrition_recettes[id_recette]
            ingredients = ingredients_recettes[id_recette]

            # Les contraintes nutritionnelles
            satisfy(
                calories * choix_recettes[id_recette] <= profil_utilisateur['calories'],
                proteines * choix_recettes[id_recette] <= profil_utilisateur['proteins'],
                glucides * choix_recettes[id_recette] <= profil_utilisateur['carbs']
            )

            # La contrainte pour vérifier si tous les ingrédients sont disponibles
            for ingredient in ingredients:
                satisfy(ingredient in ingredients_utilisateur)

    
    # Fonction objectif (ex: maximiser les protéines, les glucides, etc.)
    maximize(
        recettes[i][1] * choix_recettes[i] for i in range(len(recettes))
    )
    maximize(
        recettes[i][2] * choix_recettes[i] for i in range(len(recettes))
    )
    maximize(
        recettes[i][3] * choix_recettes[i] for i in range(len(recettes))
    )
    
    """