# Demande à l'utilisateur d'entrer le nombre de notes à saisir
nb = int(input("Entrez le nombre de notes à saisir : "))

# Redimensionnement du tableau t
t = [0] * nb

# Lecture des notes
for i in range(nb):
    t[i] = float(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Calcul de la somme des notes
somme = 0
for i in range(nb):
    somme += t[i]

# Calcul de la moyenne
moyenne = somme / nb

# Comptage du nombre d'élèves dépassant la moyenne
nbsup = 0
for i in range(nb):
    if t[i] > moyenne:
        nbsup += 1

# Affichage du nombre d'élèves dépassant la moyenne
print(nbsup, "élèves dépassent la moyenne de la classe")