from Produit import Produit

class ProduitLuxe(Produit):
    """ Hérite de Produit et surcharge de la méthode calculer_tva pour une taxe de luxe"""
    def calculer_tva(self, taux):
        """ Surcharge : Calcule la TVA avec un supplément pour les produits de luxe """
        # 1. Calcul de la TVA standard (méthode du parent)
        tva_standard = super().calculer_tva(taux)

        #2. Ajout du supplément de luxe (10% du prix unitaire + TVA standard)
        taxe_luxe = (tva_standard + (self.get_prix_unitaire())) * 0.10

        return tva_standard + taxe_luxe