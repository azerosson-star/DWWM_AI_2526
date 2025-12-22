from flask import Blueprint, render_template, request, redirect, url_for, flash
from library_app.models.database import db
from library_app.models.emprunt_model import Emprunt
from library_app.models.adherent_model import Adherent
from library_app.models.exemplaire_model import Exemplaire
from library_app.controllers.adherent_controller import admin_required # Pour l'accès admin
from datetime import datetime, timedelta
from flask_login import login_required, current_user

# Création du Blueprint
pret_bp = Blueprint('pret_bp', __name__, url_prefix='/prets')

# Durée de prêt fixe (21 jours)
DUREE_PRET_JOURS = 21

# ===============================================
# 1. LISTE DES PRÊTS ACTIFS (ADMIN/ADHERENT)
# ===============================================

@pret_bp.route('/', methods=['GET'])
@login_required
def list_emprunts():
    """
    Affiche la liste des emprunts. 
    - Admin : tous les emprunts actifs, avec possibilité de recherche.
    - Adhérent : ses propres emprunts actifs.
    """
    
    # Récupère le terme de recherche de l'URL (ex: /prets?search=Dupont)
    search_query = request.args.get('search', '').strip() 
    
    # Requête de base pour les emprunts actifs
    base_query = Emprunt.query.filter(Emprunt.date_retour_effective == None)
    
    emprunts = []
    
    if current_user.role == 'admin':
        # Logique Admin
        if search_query:
            search_pattern = f'%{search_query}%'
            # Filtre les emprunts actifs en joignant la table Adherent et en filtrant par nom ou prénom
            emprunts = base_query.join(Adherent).filter(
                db.or_(
                    Adherent.nom.like(search_pattern),
                    Adherent.prenom.like(search_pattern)
                )
            ).all()
        else:
            # Si pas de recherche, récupère tous les emprunts actifs
            emprunts = base_query.all()
            
        page_title = "Gestion des Prêts Actifs"
        
    else:
        # Logique Adhérent (pas de recherche nécessaire sur ses propres prêts)
        adherent = Adherent.query.filter_by(id_user=current_user.id_user).first()
        if adherent:
            emprunts = base_query.filter(Emprunt.num_adherent == adherent.num_adherent).all()
            page_title = "Mes Emprunts Actifs"
        else:
            flash("Vous n'êtes pas enregistré comme adhérent.", 'warning')
            return redirect(url_for('main_bp.index'))
            
    return render_template(
        'pret/list_emprunts.html', 
        emprunts=emprunts, 
        page_title=page_title,
        is_admin = current_user.role == 'admin',
        search_query=search_query # IMPORTANT : passe le terme de recherche au template
    )

# ===============================================
# 2. ENREGISTRER UN PRÊT (CREATE)
# ===============================================

@pret_bp.route('/emprunter', methods=['GET', 'POST'])
@admin_required # Seuls les administrateurs peuvent enregistrer des prêts
def emprunter():
    """Enregistre un nouvel emprunt."""

    if request.method == 'POST':
        try:
            num_adherent = request.form.get('num_adherent', type=int)
            num_inventaire = request.form.get('num_inventaire', type=int)
            
            # 1. Vérifications préliminaires
            adherent = Adherent.query.get(num_adherent)
            exemplaire = Exemplaire.query.get(num_inventaire)

            if not adherent:
                flash(f"Adhérent N°{num_adherent} introuvable.", 'danger')
                return redirect(url_for('pret_bp.emprunter'))

            if not exemplaire:
                flash(f"Exemplaire N°{num_inventaire} introuvable.", 'danger')
                return redirect(url_for('pret_bp.emprunter'))
            
            # 2. Contraintes de gestion
            
            # a) Est-ce que l'exemplaire est pour le prêt ?
            if exemplaire.type_usage != 'prêt':
                flash(f"L'exemplaire N°{num_inventaire} est destiné à la vente et ne peut pas être emprunté.", 'danger')
                return redirect(url_for('pret_bp.emprunter'))

            # b) L'exemplaire est-il disponible ? (non déjà emprunté)
            if not exemplaire.is_disponible_au_pret():
                flash(f"L'exemplaire N°{num_inventaire} est déjà en cours d'emprunt.", 'danger')
                return redirect(url_for('pret_bp.emprunter'))

            # c) L'adhérent a-t-il atteint la limite de 5 emprunts ?
            if adherent.get_emprunts_actifs() >= 5:
                flash(f"L'adhérent '{adherent.nom} {adherent.prenom}' a atteint la limite de 5 emprunts actifs.", 'danger')
                return redirect(url_for('pret_bp.emprunter'))

            # 3. Enregistrement de l'emprunt
            date_emprunt = datetime.utcnow().date()
            date_retour_prevue = date_emprunt + timedelta(days=DUREE_PRET_JOURS)
            
            nouveau_emprunt = Emprunt(
                num_adherent=num_adherent,
                num_inventaire=num_inventaire,
                date_emprunt=date_emprunt,
                date_retour_prevue=date_retour_prevue
            )
            
            db.session.add(nouveau_emprunt)
            db.session.commit()
            
            flash(f"Prêt enregistré: '{exemplaire.livre.titre}' pour {adherent.nom}. Date de retour prévue: {date_retour_prevue.strftime('%d/%m/%Y')}.", 'success')
            return redirect(url_for('pret_bp.list_emprunts'))

        except Exception as e:
            db.session.rollback()
            flash(f"Erreur inattendue lors de l'enregistrement du prêt : {e}", 'danger')
            return redirect(url_for('pret_bp.emprunter'))

    # GET : Affichage du formulaire d'emprunt
    return render_template('pret/emprunter.html', page_title='Enregistrer un Prêt')

# ===============================================
# 3. ENREGISTRER UN RETOUR (UPDATE)
# ===============================================

@pret_bp.route('/retourner/<int:num_emprunt>', methods=['POST'])
@admin_required # Seuls les administrateurs enregistrent les retours
def retourner(num_emprunt):
    """Enregistre la date de retour effective d'un emprunt."""

    emprunt = Emprunt.query.get_or_404(num_emprunt)
    
    if emprunt.date_retour_effectif is not None:
        flash(f"L'emprunt N°{num_emprunt} a déjà été marqué comme retourné le {emprunt.date_retour_effectif.strftime('%d/%m/%Y')}.", 'warning')
        return redirect(url_for('pret_bp.list_emprunts'))

    try:
        emprunt.date_retour_effectif = datetime.utcnow().date()
        db.session.commit()
        
        # Calcul des jours de retard (facultatif, mais utile)
        retard = (emprunt.date_retour_effectif - emprunt.date_retour_prevue).days
        
        message = f"Retour enregistré pour l'emprunt N°{num_emprunt} (Exemplaire: {emprunt.num_inventaire})."
        
        if retard > 0:
            message += f" ATTENTION: Retour effectué avec {retard} jour(s) de retard."
            flash(message, 'warning')
        else:
            flash(message, 'success')

    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de l'enregistrement du retour : {e}", 'danger')

    return redirect(url_for('pret_bp.list_emprunts'))

# ===============================================
# 4. FICHE DÉTAILLÉE DU PRÊT (Optionnel)
# ===============================================

@pret_bp.route('/detail/<int:num_emprunt>', methods=['GET'])
@login_required
def detail_emprunt(num_emprunt):
    """Affiche les détails d'un emprunt spécifique."""
    
    emprunt = Emprunt.query.get_or_404(num_emprunt)
    
    # Vérification d'autorisation (non-admin ne peut voir que ses propres prêts)
    if current_user.role != 'admin':
        adherent = Adherent.query.filter_by(id_user=current_user.id_user).first()
        if not adherent or emprunt.num_adherent != adherent.num_adherent:
            flash("Accès non autorisé à cet emprunt.", 'danger')
            return redirect(url_for('pret_bp.list_emprunts'))

    return render_template(
        'pret/detail_emprunt.html', 
        emprunt=emprunt, 
        page_title=f"Détail Emprunt N°{num_emprunt}"
    )