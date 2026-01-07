from flask import Blueprint, render_template, request, redirect, url_for, flash
from library_app.models.database import db
from library_app.models.adherent_model import Adherent
from library_app.models.user_model import User
# Importation des outils de sécurité de Flask-Login
from flask_login import login_required, current_user 
from werkzeug.security import generate_password_hash # Pour créer l'utilisateur lié
from functools import wraps # <-- NOUVEL IMPORT NÉCESSAIRE

# Création du Blueprint
adherent_bp = Blueprint('adherent_bp', __name__, url_prefix='/adherents')

# --- Décorateur pour vérifier le rôle Admin (Contrôle d'accès) ---

# Ce décorateur doit être défini dans un fichier utilitaire, 
# mais nous le laissons ici pour l'exemple.
def admin_required(f):
    """Vérifie si l'utilisateur connecté est un administrateur."""
    @wraps(f) # <-- CORRECTION : Conserve le nom de la fonction originale (list_adherents, add_adherent, etc.)
    @login_required
    def decorated_function(*args, **kwargs):
        # Assurez-vous que current_user et son rôle sont disponibles via Flask-Login
        if current_user.role != 'admin':
            flash('Accès non autorisé. Vous devez être administrateur.', 'danger')
            return redirect(url_for('main_bp.index')) # Rediriger vers l'accueil
        return f(*args, **kwargs)
    return decorated_function


# ===============================================
# 1. LISTE DES ADHÉRENTS (READ ALL)
# ===============================================

@adherent_bp.route('/', methods=['GET'])
@admin_required # Seuls les admins peuvent voir la liste complète
def list_adherents():
    """Affiche la liste de tous les adhérents."""
    
    # 1. Récupérer tous les adhérents
    adherents = Adherent.query.all()
    
    # 2. Rendre le template
    return render_template(
        'adherent/list.html', 
        adherents=adherents, 
        page_title='Gestion des Adhérents'
    )


# ===============================================
# 2. AJOUTER UN ADHÉRENT (CREATE)
# ===============================================

@adherent_bp.route('/add', methods=['GET', 'POST'])
@admin_required # Seuls les admins peuvent ajouter des adhérents
def add_adherent():
    """Ajoute un nouvel adhérent (et son compte utilisateur lié)."""
    
    if request.method == 'POST':
        try:
            # 1. Récupérer les données de l'Adhérent
            data = request.form
            nom = data.get('nom')
            prenom = data.get('prenom')
            email = data.get('email') # Utilisé pour créer le User
            telephone = data.get('telephone')
            
            # Adresse complète (selon notre Modèle)
            rue = data.get('rue')
            ville = data.get('ville')
            code_postal = data.get('code_postal')

            # --- Création du Compte Utilisateur (users) ---
            # Crée un User minimal avec un rôle 'user'
            if User.query.filter_by(email=email).first():
                flash(f"Un compte existe déjà avec l'email : {email}.", 'warning')
                return render_template('adherent/add.html', data=data)

            # Générer un mot de passe temporaire (ou utiliser une fonction d'envoi de mail)
            temp_password = generate_password_hash("password_initiale") 
            
            new_user = User(
                username=prenom + nom, # Nom par défaut pour l'utilisateur
                email=email,
                password=temp_password,
                role='user' # Par défaut
            )
            db.session.add(new_user)
            db.session.flush() # Récupère id_user avant le commit
            
            # --- Création de l'Adhérent (adherent) ---
            new_adherent = Adherent(
                id_user=new_user.id_user,
                nom=nom,
                prenom=prenom,
                rue=rue,
                ville=ville,
                code_postal=code_postal,
                telephone=telephone
            )
            db.session.add(new_adherent)
            db.session.commit()
            
            flash(f"Adhérent '{prenom} {nom}' (N° {new_adherent.num_adherent}) créé avec succès.", 'success')
            return redirect(url_for('adherent_bp.list_adherents'))

        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de l'ajout de l'adhérent : {e}", 'danger')
            return render_template('adherent/add.html', data=request.form)

    # GET : Affichage du formulaire d'ajout
    return render_template('adherent/add.html', page_title='Ajouter un Adhérent')


# ===============================================
# 3. ÉDITER UN ADHÉRENT (UPDATE)
# ===============================================

@adherent_bp.route('/edit/<int:num_adherent>', methods=['GET', 'POST'])
@admin_required
def edit_adherent(num_adherent):
    """Modifie les informations d'un adhérent."""
    
    adherent = Adherent.query.get_or_404(num_adherent)
    
    if request.method == 'POST':
        try:
            # 1. Récupérer les données du formulaire
            data = request.form
            
            # 2. Mettre à jour les informations de l'Adhérent
            adherent.nom = data.get('nom')
            adherent.prenom = data.get('prenom')
            adherent.rue = data.get('rue')
            adherent.ville = data.get('ville')
            adherent.code_postal = data.get('code_postal')
            adherent.telephone = data.get('telephone')
            
            # Optionnel : Mettre à jour l'email et le username dans la table User liée
            user_account = User.query.get(adherent.id_user)
            if user_account:
                user_account.email = data.get('email')
                user_account.username = data.get('prenom') + data.get('nom') # Mise à jour du username

            db.session.commit()
            flash(f"Les informations de l'adhérent N° {num_adherent} ont été mises à jour.", 'success')
            return redirect(url_for('adherent_bp.list_adherents'))

        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de la modification : {e}", 'danger')

    # GET : Affichage du formulaire de modification pré-rempli
    # Récupérer l'email pour le champ du formulaire
    user_email = Adherent.query.get(num_adherent).user.email
    
    return render_template(
        'adherent/edit.html', 
        adherent=adherent,
        user_email=user_email,
        page_title=f'Modifier Adhérent N°{num_adherent}'
    )


# ===============================================
# 4. SUPPRIMER UN ADHÉRENT (DELETE)
# ===============================================

@adherent_bp.route('/delete/<int:num_adherent>', methods=['POST'])
@admin_required
def delete_adherent(num_adherent):
    """Supprime un adhérent et son compte utilisateur lié."""
    
    adherent = Adherent.query.get_or_404(num_adherent)
    user_account = User.query.get(adherent.id_user)
    
    # Vérification : S'assurer qu'il n'y a pas d'emprunts actifs
    if adherent.get_emprunts_actifs() > 0:
        flash("Impossible de supprimer cet adhérent : il a des emprunts actifs en cours.", 'danger')
        return redirect(url_for('adherent_bp.list_adherents'))

    try:
        db.session.delete(adherent)
        # Supprimer le User compte aussi, car la relation est 1-à-1
        if user_account:
            db.session.delete(user_account)
        
        db.session.commit()
        flash(f"L'adhérent N° {num_adherent} a été supprimé ainsi que son compte utilisateur.", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de la suppression : {e}", 'danger')

    return redirect(url_for('adherent_bp.list_adherents'))