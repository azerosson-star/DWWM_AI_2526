# 1. IMPORTS
# Importation du module principal de Flask et des outils nécessaires
from flask import Blueprint, render_template, request, redirect, url_for, flash
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
    if request.method == 'POST':
        # 1. Récupérer les données du formulaire
        email = request.form.get('email')
        password = request.form.get('password')

        # 2. Logique d'authentification (sera implémentée avec SQLAlchemy)
        user = User.authenticate(email, password)
        
        if user:
            # Mettre l'utilisateur en session (Flask-Login)
            flash('Connexion réussie!', 'success')
            # Redirection vers la page d'accueil ou le tableau de bord
            return redirect(url_for('main_bp.index')) 
        else:
            flash('Email ou mot de passe incorrect.', 'danger')
            return render_template('login.html')

        #flash(f'Tentative de connexion pour {email} en attente de la logique BDD.', 'info')
        # Pour le moment, on retourne juste le template après le flash pour tester
        # return redirect(url_for('user_bp.login'))


    # Affichage de la vue (Template HTML)
    return render_template('login.html', page_title='Connexion')

# La route de déconnexion (logout) sera également ajoutée ici
# @user_bp.route('/logout')
# def logout():
#     # Logique de déconnexion (suppression de la session)
#     flash('Vous êtes déconnecté.', 'info')
#     return redirect(url_for('user_bp.login'))