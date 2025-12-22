from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from library_app.models.adherent_model import Adherent
from library_app.models.livre_model import Livre
from library_app.models.emprunt_model import Emprunt

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

@main_bp.route('/dashboard')
@login_required # Oblige l'utilisateur à être connecté
def dashboard():
    """
    Page d'administration (Dashboard). Accessible uniquement par les admins.
    """
    # **LOGIQUE CLÉ : Vérification du Rôle Admin**
    if not current_user.is_admin():
        flash('Accès non autorisé. Vous devez être administrateur.', 'danger')
        return redirect(url_for('main_bp.index'))

    # 1. Compter les adhérents totaux
    count_adherents = Adherent.query.count()
    
    # 2. Compter les livres dans le catalogue
    count_livres = Livre.query.count()
    
    # 3. Compter les prêts en cours (où la date de retour est nulle)
    count_prets = Emprunt.query.filter_by(date_retour_effective=None).count()

    # Si l'utilisateur est admin, il accède au dashboard
    return render_template('dashboard.html', page_title='Tableau de Bord Admin',
                            total_adherents=count_adherents,
                            total_livres=count_livres,
                            total_prets=count_prets)