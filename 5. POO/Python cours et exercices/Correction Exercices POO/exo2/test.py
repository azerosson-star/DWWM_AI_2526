import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from ProduitAlimentaire import ProduitAlimentaire
from datetime import date

date_aujourd_hui = date.today()
date_passee = date(2025, 11, 28) # date avant expiration
date_future = date(2026, 1, 1)   # date après expiration

# création d'un objet ProduitAlimentaire

# mon_produit_alimentaire = ProduitAlimentaire("Yaourt", 2.5, date_passee)
mon_produit_alimentaire = ProduitAlimentaire("Fromage", 5.0, date_future)

print("--- Exercice 2 : Héritage --")
print(f"Nom du produit alimentaire: {mon_produit_alimentaire.nom}, Expiration: {mon_produit_alimentaire.date_expiration}")
if mon_produit_alimentaire.est_perime(date_aujourd_hui):
    print(f"le produit : {mon_produit_alimentaire.nom} est périmé {date_aujourd_hui}.")
else:
    print(f"le produit : {mon_produit_alimentaire.nom} n'est pas périmé le {date_aujourd_hui}.")