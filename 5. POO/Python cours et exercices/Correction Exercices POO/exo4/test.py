import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from Bateau import Bateau
from Voiture import Voiture
from Avion import Avion

mon_bateau = Bateau()
ma_voiture = Voiture()
mon_avion = Avion()

# Fonction plymorphe pour afficher les déplacements
def simuler_deplacement(vehicule):
    """ Cette fonction utilise le polymorphisme pour appeler la méthode deplacer """
    print(vehicule.deplacer())

print("--- Exercice 4 : Polymorphisme ---")
simuler_deplacement(mon_bateau)
simuler_deplacement(ma_voiture)
simuler_deplacement(mon_avion)
print("-----------------------------------")