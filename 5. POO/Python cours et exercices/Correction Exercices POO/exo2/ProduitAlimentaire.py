from Produit import Produit
from datetime import date, datetime

class ProduitAlimentaire(Produit):

    """ Hérite de Produit et ajoute une date d'expiration """
    def __init__(self, nom, prix_unitaire, date_expiration:date):
        super().__init__(nom, prix_unitaire)
        self.date_expiration = date_expiration

    def est_perime(self, date_du_jour: date) -> bool:
        """ Vérifie si le produit est périmé par rapport à la date du jour """
        return date_du_jour > self.date_expiration