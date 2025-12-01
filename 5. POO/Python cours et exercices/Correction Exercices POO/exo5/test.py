import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Utilisation des classes Produit, ProduitAlimentaire et ProduitLuxe

from Produit import Produit
from ProduitAlimentaire import ProduitAlimentaire
from ProduitLuxe import ProduitLuxe
from datetime import date

date_aujourd_hui = date.today()
date_passee = date(2025, 11, 28) # date avant expiration
date_future = date(2026, 1, 1)   # date après expiration


# 2. Collection (Liste) de produits divers
panier = [
    Produit("Stylo", 1.5),
    ProduitAlimentaire("Fromage", 5.0, date_future),
    ProduitLuxe("Montre de luxe", 2500.0)
]

taux = 0.20  # Taux de TVA standard de 20%
total_taxe = 0.0

# 3. Calcul Polymorphe
for article in panier:
    # .claculer_tva() s'adapte selon le type d'article
    taxe = article.calculer_tva(taux)
    total_taxe += taxe
    # 4. Affichage00
    print(f"- {article.nom} : Taxe calculée = {taxe:.2f} €")

