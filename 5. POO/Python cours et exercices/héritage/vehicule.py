class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.moteur_allume = False

    def demarrer(self):
        if not self.moteur_allume:
            self.moteur_allume = True
            print(f"Le moteur de la {self.marque} {self.modele} est démarré.")
        else:
            print(f"Le moteur de la {self.marque} {self.modele} est déjà allumé.")

    def arreter(self):
        if self.moteur_allume:
            self.moteur_allume = False
            print(f"Le moteur de la {self.marque} {self.modele} est arrêté.")
        else:
            print(f"Le moteur de la {self.marque} {self.modele} est déjà éteint.")

    