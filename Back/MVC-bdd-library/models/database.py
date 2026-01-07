# Configuration de SQLAlchemy (db instance)
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialisation de l'instance SQLAlchemy.
# Cet objet 'db' sera importé par tous les modèles (User, Adherent, Livre, etc.)
db = SQLAlchemy()

def configure_db(app: Flask):
    """
    Configure et initialise la base de données (SQLAlchemy) pour l'application Flask.
    
    Cette fonction lit l'URI de la base de données depuis la configuration de l'application.
    """
    
    # L'URI de la BDD est lue depuis la configuration (config.py).
    # Assurez-vous que l'URI dans config.py est correcte, par exemple:
    # 'mysql+pymysql://user:password@localhost:3306/library'
    # La configuration est déjà faite dans app.py, ici on l'applique à l'instance db.
    
    # 1. Applique la configuration de la BDD
    # Ces configurations (SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS)
    # doivent être définies dans votre fichier config.py.
    
    # 2. Initialise l'extension SQLAlchemy avec l'application Flask
    db.init_app(app)

# Note: Il n'est pas nécessaire de créer les tables ici, car cela est géré
# dans le contexte de l'application dans app.py via db.create_all().