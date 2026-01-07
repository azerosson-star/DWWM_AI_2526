class Produit():
    def __init__(self, nom, prix_unitaire):
        self.nom = nom
        # Encapsulation par convention : __ indique que l'attribut est privé
        self.__prix_unitaire = prix_unitaire

    def calculer_tva(self, taux):
        """ Calcule le montant de la TVA """
        return self.__prix_unitaire * taux

    def get_prix_unitaire(self):
        """ Getter pour le prix unitaire """
        return self.__prix_unitaire