# Saisie du nombre de valeurs
nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau t
t = [0] * nb

# Saisie des valeurs dans le tableau
for i in range(nb):
    t[i] = int(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Initialisation du drapeau (flag) à true
flag = True

# Vérification si les nombres sont consécutifs
for i in range(1, nb):
    if t[i] != t[i - 1] + 1:
        flag = False
        break

# Affichage du résultat
if flag:
    print("Les nombres sont consécutifs")
else:
    print("Les nombres ne sont pas consécutifs")