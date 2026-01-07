import os
# Importe la fonction d'usine (factory function) qui configure l'application
from library_app import create_app  
# Importe l'instance de base de données
from library_app.models.database import db 

# --- Importation des modèles pour la création des tables ---
# Il est essentiel d'importer tous les modèles ici pour que SQLAlchemy les reconnaisse 
# lors de l'appel à db.create_all().
from library_app.models import user_model, adherent_model, livre_model, exemplaire_model, emprunt_model 

# 1. Instanciation de l'application
# L'objet 'app' est créé, configuré et prêt à être utilisé.
app = create_app()

# 2. Création des tables de la base de données (pour le développement)
with app.app_context():
    # Cette commande crée toutes les tables définies dans les modèles s'elles n'existent pas.
    db.create_all()
    print("Base de données et tables vérifiées et/ou créées avec succès.")


# 3. Point d'entrée principal
if __name__ == '__main__':
    # Lance l'application en mode développement. 
    # Le mode debug est généralement défini dans config.py.
    app.run()