from pycsp3 import *
import json

def charger_recettes(chemin_fichier_json):
    with open(chemin_fichier_json, 'r') as file:
        data = json.load(file)
        recettes = []
        for recette in data["recipes"]:
            id_recette = recette["id"]
            nutrition = recette["nutrition"][0]  # Supposons que le premier élément contient les données nutritionnelles
            calories = float(nutrition["calories"].replace("kcal", "").strip())
            proteines = float(nutrition["protein"].replace("g", "").strip())
            glucides = float(nutrition["carbs"].replace("g", "").strip())
            recettes.append((id_recette, calories, proteines, glucides))
        return recettes





if __name__ == '__main__':
    # Supposons que nous ayons 3 recettes avec leurs valeurs nutritionnelles
    recettes = charger_recettes('../Data/dataset_nutrition.json')

    # Création des variables
    choix_recettes = VarArray(size=len(recettes), dom={0, 1})

    # Contraintes (ex: ne pas dépasser 1200 calories)
    satisfy(
        Sum(recettes[i][0] * choix_recettes[i] for i in range(3)) <= 1200
    )

    # Fonction objectif (ex: maximiser les protéines)
    maximize(
        Sum(recettes[i][0] * choix_recettes[i] for i in range(3))
    )

    if solve() == SAT:
        for i, val in enumerate(choix_recettes):
            if val.value() == 1:
                print(
                    f"Recette choisie: ID={recettes[i][0]}, Calories={recettes[i][1]}, Proteines={recettes[i][2]}, Glucides={recettes[i][3]}")
