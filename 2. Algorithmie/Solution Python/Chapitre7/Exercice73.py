# Saisie du nombre de valeurs
nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau t
t = [0] * nb

# Saisie des valeurs dans le tableau
for i in range(nb):
    t[i] = int(input(f"Entrez le nombre n° { str(i + 1) } : "))

# Inversion des éléments du tableau
for i in range(nb // 2):
    t[i], t[nb-1-i]  = t[nb-1-i] , t[i]

    # temp = t[i]
    # t[i] = t[nb - 1 - i]
    # t[nb - 1 - i] = temp

# Affichage du tableau après inversion
print("tableau après inversion :", t)