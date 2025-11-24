# Dictionnaire vide 
utilisateur_vide = {} 
# Dictionnaire pré-rempli (exemple d'un livre) 
livre = { 
    "titre": "L'Étranger", 
    "auteur": "Albert Camus", 
    "année": 1942, 
    "pages": 160
} 

print(livre) 

# Ajouter une nouvelle paire clé-valeur 
# del livre["prix"]
livre["prix"] = 9.99 
print(livre) 

# Supprimer une paire clé-valeur
livre.pop("pages")
print(livre)

# Itération sur les paires (clé, valeur) 
for cle, valeur in livre.items(): 
    print(f"{cle.capitalize()}: {valeur}") 

if "auteur" in livre: 
    print("L'auteur est renseigné.") 

if "pages" not in livre: 
    print("Le nombre de pages n'est pas renseigné.")

if 1942 in livre.values(): 
    print("Cette année fait partie des valeurs.") 

if 1943 not in livre.values(): 
    print("Cette année ne fait pas partie des valeurs.") 