# Super-classe (Classe Parent) 
class Animal: 
    def __init__(self, nom): 
        self.nom = nom 
    def respirer(self): 
        return f"{self.nom} respire." 
    
# Sous-classe (Classe Enfant) qui hérite d'Animal 
class Chat(Animal): 
    def __init__(self, nom, couleur): 
    # Appel du constructeur de la classe Parent 
        super().__init__(nom) 
        self.couleur = couleur 
        
    # Nouvelle méthode propre à la classe Chat 
    def miauler(self): 
        return f"{self.nom} ({self.couleur}) miaule." 

    # Exemple d'utilisation du Polymorphisme 
    def faire_respirer(animal): 
        # Appelle la méthode 'respirer' spécifique à l'objet passé 
        print(animal.respirer()) 

    
class Chien(Animal): 
    def __init__(self, nom): 
        super().__init__(nom) 
    # Surcharge de la méthode 'respirer' du Parent (Animal) 
    def respirer(self): 
        return f"{self.nom} halete et respire bruyamment." # Implémentation différente 

    # Exemple d'utilisation du Polymorphisme 
    def faire_respirer(animal): 
        # Appelle la méthode 'respirer' spécifique à l'objet passé 
        print(animal.respirer()) 

#rex = Chien("Rex") 
#mistigri = Chat("Mistigri", "Blanc") 

#print(rex.faire_respirer())


# Affiche l'implémentation de Chien 
print(mistigri.faire_respirer()) # Affiche l'implémentation de Chat (héritée d'Animal)


# Instanciation de l'objet Chat
mon_chat = Chat("Mistigri", "Noir")
print(mon_chat.respirer()) # Méthode héritée
print(mon_chat.miauler())  # Méthode propre
print(mistigri.faire_respirer()) # Polymorphisme avec Chat
# Instanciation de l'objet Chien
mon_chien = Chien("Rex")
print(mon_chien.respirer()) # Méthode surchargée
print(mon_chien.faire_respirer()) # Polymorphisme avec Chien

