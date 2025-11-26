from vehicule import Vehicule

class Voiture(Vehicule):
    def __init__(self, marque, modele, nombre_portes):
        # Appel du constructeur de la classe parente
        super().__init__(marque, modele)
        self.nombre_portes = nombre_portes # Attribut propre à la classe Voiture

    def klaxonner(self):
        if self.moteur_allume:
            print(f"La {self.marque} {self.modele} klaxonne : Tuut tuut !")
        else:
            print(f"La {self.marque} {self.modele} ne peut pas klaxonner, le moteur est éteint.")