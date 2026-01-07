# Déclaration du tableau n
n = [0] * 7

# Initialisation de la première valeur
n[0] = 1

# Remplissage du tableau selon la formule n[k] = n[k-1] + 2
for k in range(1, 7):
    n[k] = n[k-1] + 2

# Affichage des éléments du tableau
for i in range(7):
    print(n[i])