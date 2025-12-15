from flask import Blueprint, render_template
from flask_login import current_user

# Crée une instance de Blueprint. 
# Le préfixe d'URL ('/') signifie que les routes définies ici 
# ne nécessitent pas de préfixe supplémentaire (ex: /index, /about).
main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    """
    Route pour la page d'accueil de la librairie.
    (Alternative à la route '/' directement dans app.py)
    """
    # Utilise la vue (V) 'index.html' depuis le dossier app/views/templates/
    # Note : Dans votre configuration app.py[cite: 71], la route '/' est déjà définie.
    # On pourrait la déplacer ici, mais nous allons conserver la route '/index' pour cet exemple.
    return render_template('index.html', title='Accueil de la Librairie')

@main_bp.route('/about')
def about():
    """
    Route pour la page 'À propos' de l'application.
    """
    # Suppose que vous avez un fichier app/views/templates/about.html
    return render_template('about.html', title='À Propos')

# Exemple d'une page de contact
@main_bp.route('/contact')
def contact():
    """
    Route pour la page de contact.
    """
    # Suppose que vous avez un fichier app/views/templates/contact.html
    return render_template('contact.html', title='Contact')