class CompteBancaire: 
    def __init__(self, solde_initial): 
        # Attribut "privé" par convention pour  l'encapsulation 
        self.__solde = solde_initial  
        # Méthode "publique" pour accéder aux données (Abstraction) 

    def deposer(self, montant): 
        if montant > 0: 
            self.__solde += montant 
            
    def get_solde(self): 
        return self.__solde 

# Instanciation de l'objet 
mon_compte = CompteBancaire(1000)

# Dépôt d'argent 
mon_compte.deposer(500)

# Accès au solde via la méthode publique 
print(f"Solde du compte : {mon_compte.get_solde()}")

# Tentative d'accès direct à l'attribut privé (devrait échouer)
# print(mon_compte.__solde)  # Ceci générera une erreur d'attribut
