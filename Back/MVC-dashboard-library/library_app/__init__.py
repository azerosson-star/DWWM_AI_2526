from flask import Flask
from flask_login import LoginManager
# Importation de l'instance SQLAlchemy
from library_app.models.database import db 
# Importation de la configuration
from library_app.config import Config
# Importation des Modèles (nécessaire pour Flask-Login)
from library_app.models.user_model import User 

# Importation des Blueprints (Contrôleurs)
from library_app.controllers.user_controller import user_bp
from library_app.controllers.main_controller import main_bp 
from library_app.controllers.adherent_controller import adherent_bp # NOUVEL IMPORT
from library_app.controllers.catalogue_controller import catalogue_bp
from library_app.controllers.pret_controller import pret_bp # NOUVEL IMPORT

# ... Initialisation de LoginManager ...
login_manager = LoginManager()

login_manager.login_view = 'user_bp.login' # Définit la route de connexion

# Personnaliser le message d'erreur si l'utilisateur est redirigé
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'
login_manager.login_message_category = 'info'

# Fonction pour recharger l'objet User à partir de l'ID stocké dans la session
@login_manager.user_loader
def load_user(user_id):
    """
    Fonction de rappel utilisée par Flask-Login pour charger un utilisateur 
    depuis l'ID stocké dans la session.
    """
    # Utilise l'ID pour retrouver l'utilisateur dans la BDD
    return User.query.get(int(user_id)) # Utilise la méthode get du modèle User


def create_app(config_class=Config):
    """
    Fonction d'usine (Factory Function) pour créer et configurer l'application Flask.
    """
    app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
    
    # 1. Configuration
    app.config.from_object(config_class)

    # 2. Initialisation des extensions
    db.init_app(app)
    login_manager.init_app(app) # Initialisation de Flask-Login

    # 3. Enregistrement des Blueprints (Routes)
    
    # Routes d'Authentification (/auth/login, /auth/register)
    app.register_blueprint(user_bp) 
    
    # Routes principales (/index, /about)
    app.register_blueprint(main_bp) 
    
    # Routes de Gestion des Adhérents (/adherents/...) - NOUVEL ENREGISTREMENT
    app.register_blueprint(adherent_bp) 

    app.register_blueprint(catalogue_bp)

    app.register_blueprint(pret_bp) # <-- NOUVEL ENREGISTREMENT

    # Note: La création des tables (db.create_all()) se fait généralement 
    # via un script CLI ou dans app.py.

    return app