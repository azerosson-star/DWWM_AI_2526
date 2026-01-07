import os
from flask import Flask
from flask_login import LoginManager

#from controllers.user_controller import user_bp
from controllers.main_controller import main_bp
from models.user_model import User


app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
app.secret_key = 'votre_clé_secrète_unique_et_sécurisée'  # Définir la clé secrète de l'application

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

#app.register_blueprint(user_bp)
app.register_blueprint(main_bp)


# Point d'entrée principal pour l'exécution
if __name__ == '__main__':
    # load_dotenv() # Décommenter si vous utilisez un fichier .env
    app.run(debug=True)