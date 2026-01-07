class Rectangle:
    def __init__ (self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def calculer_surface(self):
        return self.largeur * self.longueur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.longueur)

# Instanciation de l'objet Rectangle
mon_rectangle = Rectangle(25, 100)
print(f"Surface du rectangle : {mon_rectangle.calculer_surface()}")
print(f"Périmètre du rectangle : {mon_rectangle.calculer_perimetre()}")