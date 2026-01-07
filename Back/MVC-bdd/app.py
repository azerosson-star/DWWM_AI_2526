from flask import Flask
from controllers.main_controller import MainController
from controllers.user_controller import UserController
from config import Config, db

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
app.secret_key = 'votre_clé_secrète_unique_et_sécurisée'  # Définir la clé secrète de l'application
Config.init_app(app)

@app.route('/')
def index():
    return MainController.index()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return UserController.login()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return UserController.register()

if __name__ == '__main__':
    app.run(debug=True)