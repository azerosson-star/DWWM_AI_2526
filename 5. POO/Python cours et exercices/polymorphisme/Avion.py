# Une classe pour une machine capable de voler 
class Avion:
    def __init__(self, modele, compagnie, capacite):
        self.modele = modele
        self.compagnie = compagnie
        self.capacite = capacite

    def voler(self):
        print(f"L'avion {self.modele} de la compagnie {self.compagnie} décolle et prend de l'altitude.")

    def atterrir(self):
        print(f"L'avion {self.modele} de la compagnie {self.compagnie} atterrit en toute sécurité.")