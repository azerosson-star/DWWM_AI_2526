# Déclaration des variables nb, nbpos, nbneg
nb = 0
nbpos = 0
nbneg = 0

# Demande à l'utilisateur le nombre de valeurs
print("Entrez le nombre de valeurs :")
nb = int(input())

# Redimensionnement du tableau T
t = [0] * nb

# Boucle pour lire les valeurs et compter les valeurs positives et négatives
for i in range(nb):
    print("Entrez le nombre n°", i + 1)
    t[i] = float(input())
    if T[i] > 0:
        nbpos += 1
    else:
        nbneg += 1

# Affichage du nombre de valeurs positives et négatives
print("Nombre de valeurs positives :", nbpos)
print("Nombre de valeurs négatives :", nbneg)
