# FoodAssistant : Votre Compagnon Nutritionnel Personnalisé

**FoodAssistant** est un projet novateur conçu pour simplifier et améliorer votre parcours nutritionnel quotidien. En
tant que votre compagnon alimentaire personnel, l'objectif de FoodAssistant est de faciliter la réalisation de vos *
*Apports Journaliers Recommandés (AJR)** en vous fournissant des recommandations personnalisées d'aliments et de
recettes.

## Principaux Objectifs :

1. **Personnalisation Nutritionnelle :**
    - FoodAssistant prend en compte vos préférences alimentaires, restrictions alimentaires, et habitudes de cuisson
      pour créer des recommandations nutritionnelles entièrement personnalisées. Que vous suiviez un régime spécifique
      ou que vous ayez des préférences culinaires particulières, FoodAssistant s'adapte à vos besoins individuels.

2. **Suivi des Apports Journaliers :**
    - Suivez facilement vos AJR quotidiens et hebdomadaires avec l'aide de FoodAssistant. Recevez des suggestions de
      repas équilibrés qui contribuent à l'atteinte de vos objectifs nutritionnels, que ce soit pour la perte de poids,
      la prise de masse musculaire, ou simplement pour maintenir une alimentation saine.

3. **Sélection de Recettes Équilibrées :**
    - Explorez une variété de recettes soigneusement sélectionnées pour leur équilibre nutritionnel. FoodAssistant
      propose des idées pour le petit déjeuner, le déjeuner, le dîner, et même des collations, en veillant à ce que
      chaque repas contribue de manière optimale à votre bien-être nutritionnel.

4. **Gestion de l'Inventaire Alimentaire :**
    - Simplifiez votre expérience culinaire en gérant efficacement votre inventaire alimentaire. FoodAssistant peut vous
      aider à planifier des repas en fonction des ingrédients disponibles, réduisant ainsi le gaspillage alimentaire.

5. **Informations Nutritionnelles Détaillées :**
    - Accédez à des informations nutritionnelles détaillées pour chaque aliment et recette recommandée. Découvrez les
      valeurs caloriques, les apports en protéines, glucides, lipides, ainsi que les vitamines et les minéraux
      essentiels à votre bien-être.

6. **Options pour Tous les Modes Alimentaires :**
    - Que vous suiviez un régime spécifique, que vous soyez végétarien, végétalien, ou que vous ayez des besoins
      alimentaires particuliers, FoodAssistant propose des options adaptées à tous les modes alimentaires.

FoodAssistant a pour mission de simplifier la planification des repas, de vous inspirer avec des idées culinaires
variées, et de vous accompagner dans votre quête d'une alimentation équilibrée et personnalisée. Rejoignez-nous dans
cette aventure vers une vie plus saine et savoureuse avec FoodAssistant à vos côtés.

## Idées :

- Retours utilisateurs, pouce rouge/vert pour les recettes
- Prediction de la disponibilité des aliments
- Recommandation de recettes en fonction de la disponibilité des aliments
- Des jauges avec rappel pour les apports hebdomadaires

## API et datasets :

- https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/getFood , API -> nutriments/aliments
- https://rapidapi.com/spoonacular/api/recipe-food-nutrition l'API de
  recettes https://rapidapi.com/blog/build-food-website/ avec son tutoriel

## Lancement de l'appplication :
- Insallation des dépendances
- run le fichier app.py situé dans le dossier webApp
- 
## Dev :
- Python 3.10
- Flask pour la partie web
- 500 appels par jour pour l'API de recettes