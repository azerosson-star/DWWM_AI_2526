# Déclaration du tableau suite
suite = [0] * 8

# Initialisation des deux premières valeurs
suite[0] = 1
suite[1] = 1

# Remplissage du tableau selon la formule suite[i] = suite[i-1] + suite[i-2]
for i in range(2, 8):
    suite[i] = suite[i-1] + suite[i-2]

# Affichage des éléments du tableau
for i in range(8):
    print(suite[i]) # Affichage de la séquence de Fibonacci

