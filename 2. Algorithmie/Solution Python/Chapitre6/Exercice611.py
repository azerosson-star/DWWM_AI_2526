# Supposons que les tableaux t1 et t2 sont déjà saisis
t1 = [4, 8, 7, 12]  # Exemple de tableau t1 saisi
t2 = [3, 6]  # Exemple de tableau t2 saisi

# Détermination des tailles des tableaux t1 et t2
n1 = len(t1)
n2 = len(t2)

# Initialisation de la variable S
somme = 0

# Calcul du produit scalaire des tableaux t1 et t2
for i in range(n1):
    for j in range(n2):
        somme += t1[i] * t2[j]

# Affichage du résultat
print("Le schtroumpf est :", somme)