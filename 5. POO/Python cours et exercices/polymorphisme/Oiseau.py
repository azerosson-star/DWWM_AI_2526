# Une classe pour un être vivant capable de voler
class Oiseau:
    def __init__(self, nom, couleur, taille):
        self.nom = nom
        self.couleur = couleur
        self.taille = taille

    def chanter(self):
        print(f"{self.nom} chante joyeusement !")

    def voler(self):
        print(f"{self.nom} s'envole en battant des ailes !")