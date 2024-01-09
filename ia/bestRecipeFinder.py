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


if __name__ == '__main__':
    recettes = [
        (1099404, 287, 7, 59), (632614, 271, 5, 33), (635370, 273, 5, 13),
        (632539, 455, 4, 40), (642605, 365, 12, 61), (657939, 489, 14, 11),
        (661544, 219, 6, 17)
    ]

    choix_recettes = VarArray(size=len(recettes), dom=range(2))

    # Appliquer une contrainte pour chaque recette

    satisfy(
        recettes[i][1] * choix_recettes[i] <= 1000 for i in range(len(recettes))
    )

# Fonction objectif (ex: maximiser les protéines)
# maximize(
# recettes[i][1] * choix_recettes[i] for i in range(len(recettes))
