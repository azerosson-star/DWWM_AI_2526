import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from ProduitLuxe import ProduitLuxe

montre = ProduitLuxe("Montre de luxe", 5000.00)
taux_tva_standard = 0.20  # 20% de TVA

taxe_totale = montre.calculer_tva(taux_tva_standard)


print(f"Taxe standard (20%) : {montre.get_prix_unitaire() * taux_tva_standard:.2f} €")
print(f"Supplément luxe (10%) : {(montre.get_prix_unitaire() * (1 + taux_tva_standard)) * 0.10:.2f} €")
print(f"Taxe totale sur le produit de luxe : {taxe_totale:.2f} €")
#print(f"Montant total (Taxe standard + supplément luxe) : {montre.get_prix_unitaire() * (1 + taux_tva_standard) * (1 + 0.10):.2f} €")
print(f"Montant total (Prix unitaire + Taxe totale) : {montre.get_prix_unitaire() + taxe_totale:.2f} €")
