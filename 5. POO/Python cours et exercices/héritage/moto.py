from vehicule import Vehicule

class Moto(Vehicule):
    def demarrer(self):
        # Surcharge de la méthode demarrer pour les motos
        if self.moteur_allume:
            print(f"La moto {self.marque} {self.modele} vrombit déjà.")
        else:
            # Appel de la méthode demarrer de la classe parente
            super().demarrer()
            print(f"La moto {self.marque} {self.modele} vrombit fort !")