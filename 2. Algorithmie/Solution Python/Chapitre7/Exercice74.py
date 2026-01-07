# Saisie du nombre de valeurs
nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau t
t = [0] * nb

# Saisie des valeurs dans le tableau
for i in range(nb):
    t[i] = int(input(f"Entrez le nombre n° {i + 1} : "))

# Saisie du rang de la valeur à supprimer
s = int(input("Rang de la valeur à supprimer ? "))

# # Suppression de la valeur à l'indice S
# for i in range(s, nb - 1):
#     t[i] = t[i + 1]

# # Redimensionnement du tableau après suppression
# t = t[:nb - 1]
t.pop(s)

# Affichage du tableau après suppression
print("tableau après suppression :", t)