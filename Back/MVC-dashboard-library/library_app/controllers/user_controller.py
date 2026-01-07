# 1. IMPORTS
# Importation du module principal de Flask et des outils nécessaires
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user # Nouveaux imports
# Importation du Modèle Utilisateur (à créer dans models/user_model.py)
from library_app.models.user_model import User

# Création d'un Blueprint pour regrouper les routes liées aux utilisateurs
user_bp = Blueprint('user_bp', __name__, url_prefix='/auth')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Gère l'inscription d'un nouvel utilisateur (users).
    GET: Affiche le formulaire d'inscription.
    POST: Traite la soumission du formulaire et enregistre l'utilisateur.
    """
    if request.method == 'POST':
        # 1. Récupérer les données du formulaire (nom, email, mot de passe)
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # 2. Logique d'enregistrement (sera implémentée avec SQLAlchemy dans le Module)
        # Exemple de vérification :
        if User.email_exists(email):
            flash('Cet email est déjà utilisé.', 'warning')
            return render_template('register.html')
        
        # Exemple d'enregistrement :
        User.create_user(username, email, password, role='user') # Tous les nouveaux sont 'user' par défaut
        
        flash(f'Inscription réussie pour {username}. Veuillez vous connecter.', 'success')
        return redirect(url_for('user_bp.login'))

    # Affichage de la vue (Template HTML) [cite: 39]
    return render_template('register.html', page_title='Inscription')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Gère la connexion des utilisateurs.
    GET: Affiche le formulaire de connexion.
    POST: Traite la soumission du formulaire et connecte l'utilisateur.
    """
    """Gère la connexion des utilisateurs."""
    # Si l'utilisateur est déjà connecté, le rediriger vers le dashboard
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard')) # Redirection vers le dashboard
    
    if request.method == 'POST':
        # 1. Récupérer les données du formulaire
        email = request.form.get('email')
        password = request.form.get('password')

        # 2. Logique d'authentification (sera implémentée avec SQLAlchemy)
        user = User.authenticate(email, password)
        
        if user:
            # Utilisation de Flask-Login pour gérer la session
            login_user(user) 
            flash('Connexion réussie!', 'success')
            
            # **LOGIQUE CLÉ : Redirection vers le Dashboard Admin ou la page d'accueil**
            if user.is_admin():
                # L'admin va au tableau de bord des opérations CRUD
                return redirect(url_for('main_bp.dashboard')) 
            else:
                # Les utilisateurs normaux vont à l'accueil
                return redirect(url_for('main_bp.index'))
        else:
            flash('Email ou mot de passe incorrect.', 'danger')
            return render_template('login.html', page_title='Connexion')

        #flash(f'Tentative de connexion pour {email} en attente de la logique BDD.', 'info')
        # Pour le moment, on retourne juste le template après le flash pour tester
        # return redirect(url_for('user_bp.login'))


    # Affichage de la vue (Template HTML)
    return render_template('login.html', page_title='Connexion')

# La route de déconnexion (logout) sera également ajoutée ici
@user_bp.route('/logout')
@login_required # S'assurer que seul un utilisateur connecté peut se déconnecter
def logout():
#     # Logique de déconnexion (suppression de la session)
    logout_user() # Fonction de Flask-Login
    flash('Vous êtes déconnecté.', 'info')
    return redirect(url_for('user_bp.login'))

# ... (Il faudra s'assurer que les routes CRUD admin soient protégées 
# par un décorateur de rôle, par exemple dans adherent_controller.py)