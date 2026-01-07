# Configuration de SQLAlchemy (db instance)
from flask_sqlalchemy import SQLAlchemy

# Initialisation de l'instance SQLAlchemy.
# Cet objet 'db' sera importé par tous les modèles (User, Adherent, Livre, etc.)
db = SQLAlchemy()