# instanciation d'un objet Voiture et d'un objet Moto
from voiture import Voiture
from moto import Moto

ma_voiture = Voiture("Toyota", "Corolla", 4)
ma_moto = Moto("Harley-Davidson", "Street 750")

# Utilisation des méthodes de la classe Voiture
ma_voiture.demarrer() # Méthode héritée de Vehicule
ma_voiture.klaxonner() # Méthode propre à Voiture
ma_voiture.arreter() # Méthode héritée de Vehicule

# Utilisation des méthodes de la classe Moto
ma_moto.demarrer() # Méthode surchargée dans Moto

ma_moto.demarrer() # Appel à la méthode surchargée pour montrer le comportement différent
ma_moto.arreter() # Méthode héritée de Vehicule