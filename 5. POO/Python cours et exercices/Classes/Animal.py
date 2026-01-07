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
    
# Instanciation de l'objet Chat
mon_chat = Chat("Mistigri", "Noir") 
print(mon_chat.respirer()) # Méthode héritée 
print(mon_chat.miauler())  # Méthode propre