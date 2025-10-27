# Saisie du nombre de valeurs
nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau t
t = [0] * nb

# Saisie des valeurs dans le tableau
for i in range(nb):
    t[i] = int(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Saisie du rang de la valeur à supprimer
S = int(input("Rang de la valeur à supprimer ? "))

# Suppression de la valeur à l'indice S
for i in range(S, nb - 1):
    t[i] = t[i + 1]

# Redimensionnement du tableau après suppression
t = t[:nb - 1]

# Affichage du tableau après suppression
print("tableau après suppression :", t)