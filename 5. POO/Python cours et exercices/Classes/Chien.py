Class Chien :
     1. Le constructeur (Méthode spéciale pour créer 
l'objet) 0  
    def __init__(self, nom, race): 
        self.nom = nom        
        self.race = race      
    # Attribut d'instance 
# Attribut d'instance 
# 2. Une méthode d'instance 
def aboyer(self): 
return f"{self.nom} fait Wouf! Wouf!" 
# Instanciation de l'objet 
mon_chien = Chien("Rex", "Berger Allemand") 
# Accéder aux attributs 
print(f"Nom : {mon_chien.nom}, Race : {mon_chien.race}") 
# Appeler une méthode 
print(mon_chien.aboyer())  