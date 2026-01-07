# Demande à l'utilisateur d'entrer le nombre de valeurs
nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau t
t = [0] * nb

# Lecture des valeurs
for i in range(nb):
    t[i] = int(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Affichage du nouveau tableau
print("nouveau tableau :")
for i in range(nb):
    t[i] += 1
    print(t[i])
