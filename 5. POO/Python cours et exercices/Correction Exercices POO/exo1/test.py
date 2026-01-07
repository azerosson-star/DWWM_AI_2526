import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# instanciation de la classe Produit
from Produit import Produit

# création d'un objet Produit
mon_produit = Produit("Ordinateur Portable", 1200)

# Calculer de la TVA à 5% et affiche le prix unitaire du produit via la méthode get_prix_unitaire()

taux_tva = 0.05

tva_produit = mon_produit.calculer_tva(taux_tva)
print("--- Exercice 1 : Encapsulation --")
print(f"Nom du produit: {mon_produit.nom}")

print(f"Prix unitaire du produit (via getter): {mon_produit.get_prix_unitaire()} €")
print(f"Montant TVA (5%): {tva_produit:.2f} €")
print("----------------------------------------")