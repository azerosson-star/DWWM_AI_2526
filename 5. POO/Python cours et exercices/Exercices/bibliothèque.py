from Livre import Livre

# Création du Dictionnaire pour stocker les livres
bibliothèque = {}

livre_a = Livre("1984", "George Orwell", "1234567890")
livre_b = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "0987654321")
livre_c = Livre("Les Misérables", "Victor Hugo", "1122334455")

# Ajout des livres à la bibliothèque
# Utilisation de l'ISBN comme clé unique pour chaque livre
bibliothèque[livre_a.isbn] = livre_a
bibliothèque[livre_b.isbn] = livre_b
bibliothèque[livre_c.isbn] = livre_c

print(f"La bibliothèque contient {len(bibliothèque)} livres.\n")

# clé du livre_a
isbn_a = "1234567890"

# Récupération et affichage des détails du livre_a
livre_recuperer = bibliothèque.get(isbn_a)

if livre_recuperer:
    livre_recuperer.emprunter()

    # Vérification de la disponibilité après l'emprunt
    livre_recuperer.afficher_details()

# Parcourir tous les livres dans la bibliothèque et afficher leurs détails
print("\nDétails de tous les livres dans la bibliothèque :\n")
for isbn, livre in bibliothèque.items():
    etat = "Oui" if livre.disponible else "Non"
    print(f" {etat} - Titre: {livre.titre}, Auteur: {livre.auteur}, ISBN: {livre.isbn}")
    print()  # Ligne vide pour une meilleure lisibilité
