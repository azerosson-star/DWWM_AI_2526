# Déclaration des variables i, somme
somme = 0

# Supposons que le tableau T est déjà saisi
tableau = [1, 2, 3, 4, 5]  # Exemple de tableau saisi

# Calcul de la somme des éléments du tableau
for i in range(len(tableau)):
    somme += tableau[i]

# Affichage de la somme
print("somme des éléments du tableau :", somme)