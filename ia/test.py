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
    print(charger_recettes('../Data/dataset_nutrition.json'))
    data = charger_recettes('../Data/dataset_nutrition.json')
    if data[1][1] <= 1300:
        print("kys")
