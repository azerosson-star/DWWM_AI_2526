# instanciatio  des objets
from Oiseau import Oiseau
from Avion import Avion

mon_oiseau = Oiseau("Rouge-gorge", "rouge et brun", "petit")
mon_avion = Avion("Airbus A320", "Air France", 180)

print("--- Demonstration du polymorphisme ---\n")

def faire_voler(entite_volante):
    print(entite_volante.voler())


# Appel de la methode voler pour l'oiseau
faire_voler(mon_oiseau)
print("\n")

# Appel de la methode voler pour l'avion
faire_voler(mon_avion)
print("\n--- Fin de la demonstration ---")