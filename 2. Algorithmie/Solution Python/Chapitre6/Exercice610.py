# Supposons que les tableaux t1 et t2 sont déjà saisis
t1 = [4, 8, 7, 9, 1, 5, 4, 6, 7]  # Exemple de tableau t1 saisi
t2 = [7, 6, 5, 2, 1, 3, 7, 4]  # Exemple de tableau t2 saisi

# Détermination de la taille des tableaux t1 et t2
n = min(len(t1), len(t2))

# Création du tableau t3 de même taille que t1 et t2
t3 = [0] * n

# Calcul de la somme des éléments des tableaux t1 et t2
for i in range(n):
    t3[i] = t1[i] + t2[i]

# Affichage du tableau t3
print("Tableau t3 après addition de t1 et t2 :", t3)
