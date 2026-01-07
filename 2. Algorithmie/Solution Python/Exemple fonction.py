def bonjour():
    print("Bonjour")

def saluer(nom="DUPOND", prenom="Jules"):
    print(f"Bonjour {nom} {prenom}")
    
# def saluer(nom):
#     if nom==None:
#         print("Bonjour Monsieur")
#     else:
#         print(f"Bonjour {nom}")

    # APPEL
bonjour()
saluer("toto")
saluer()
saluer(prenom="titi")


