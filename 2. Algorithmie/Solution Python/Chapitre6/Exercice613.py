# Demande à l'utilisateur d'entrer le nombre de valeurs
nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau t
t = [0] * nb

# Lecture des valeurs
for i in range(nb):
    t[i] = float(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Recherche de l'élément le plus grand et de sa position
posmaxi = 0
for i in range(1, nb):
    if t[i] > t[posmaxi]:
        posmaxi = i

# Affichage de l'élément le plus grand et de sa position
print("Element le plus grand :", t[posmaxi])
print("position de cet élément :", posmaxi)