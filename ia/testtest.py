from ortools.sat.python import cp_model

# Define the data
recettes = [
    (1099404, 287, 7, 59), (632614, 271, 5, 33), (635370, 273, 5, 13),
    (632539, 455, 4, 40), (642605, 365, 12, 61), (657939, 489, 14, 11),
    (661544, 219, 6, 17)
]

# Create a constraint programming model
model = cp_model.CpModel()

# Define decision variables
choix_recettes = [model.NewIntVar(0, 1, f"choix_recette_{i}") for i in range(len(recettes))]

# Define the constraint: For each recette, the constraint is recettes[i][1] * choix_recettes[i] <= 1000
for i in range(len(recettes)):
    model.Add(recettes[i][1] * choix_recettes[i] <= 1000)

# Create a solver and solve the problem
solver = cp_model.CpSolver()
solver.Solve(model)

# Print the results
for i in range(len(recettes)):
    print(f"Recette {i+1}: Chosen = {solver.Value(choix_recettes[i])}")
