class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True # Attribut pour indiquer si le livre est disponible

    def afficher_details(self):
        etat = "Oui" if self.disponible else "Non"
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponible: {etat}")

    def emprunter(self):
        ## Change l'état de disponibilité du livre lors de l'emprunt
        if self.disponible:
            self.disponible = False
            print(f"Le livre : {self.titre} a été emprunté. Il n'est pas disponible")
        else:
            print(f"Le livre : {self.titre} est de nouveau disponible.")

    def retourner(self):
        ## Change l'état de disponibilité du livre lors du retour
        if not self.disponible:
            self.disponible = True
            print(f"Le livre : {self.titre} a été retourné. Il est maintenant disponible.")
        else:
            print(f"Le livre : {self.titre} était déjà disponible.")