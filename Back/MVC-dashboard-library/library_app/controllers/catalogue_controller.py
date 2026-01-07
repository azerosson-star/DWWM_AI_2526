from flask import Blueprint, render_template, request, redirect, url_for, flash
from library_app.models.database import db
from library_app.models.livre_model import Livre, Auteur, Ecrire
from library_app.models.exemplaire_model import Exemplaire # Pour gérer les copies
from library_app.controllers.adherent_controller import admin_required # Réutilise le décorateur

# Création du Blueprint
catalogue_bp = Blueprint('catalogue_bp', __name__, url_prefix='/catalogue')


# ===============================================
# 1. LISTE DES LIVRES (READ ALL)
# ===============================================

@catalogue_bp.route('/', methods=['GET'])
# La consultation est ouverte à tous les utilisateurs connectés
def list_livres():
    """Affiche la liste de tous les livres (l'œuvre)."""
    
    # Récupération de tous les livres, triés par titre
    livres = Livre.query.order_by(Livre.titre).all()
    
    return render_template(
        'catalogue/list_livres.html', 
        livres=livres, 
        page_title='Catalogue des Livres'
    )


# ===============================================
# 2. FICHE DÉTAILLÉE D'UN LIVRE (READ ONE)
# ===============================================

@catalogue_bp.route('/livre/<string:isbn>', methods=['GET'])
def view_livre(isbn):
    """Affiche les détails d'un livre, ses auteurs et ses exemplaires."""
    
    # Utilisation de get_or_404 pour gérer le cas où l'ISBN n'existe pas
    livre = Livre.query.get_or_404(isbn)
    
    # Les exemplaires sont récupérés via la relation définie dans le modèle Livre
    # On récupère tous les auteurs via la relation Many-to-Many
    auteurs = livre.auteurs 
    
    return render_template(
        'catalogue/view_livre.html', 
        livre=livre,
        auteurs=auteurs,
        page_title=livre.titre
    )


# ===============================================
# 3. AJOUTER/MODIFIER UN LIVRE (CREATE/UPDATE)
# ===============================================

@catalogue_bp.route('/edit_livre/<string:isbn>', methods=['GET', 'POST'])
@catalogue_bp.route('/add_livre', methods=['GET', 'POST'], defaults={'isbn': None})
@admin_required
def edit_add_livre(isbn):
    """Ajoute un nouveau livre ou modifie un livre existant."""
    
    is_edit = isbn is not None
    livre = Livre.query.get(isbn) if is_edit else Livre()
    
    # Récupérer tous les auteurs pour les afficher dans la liste déroulante/checkbox
    all_auteurs = Auteur.query.order_by(Auteur.nom).all()
    
    if request.method == 'POST':
        try:
            data = request.form
            
            # Mise à jour des champs du Livre
            if not is_edit:
                livre.isbn = data.get('isbn') # L'ISBN doit être fourni à la création
            
            livre.titre = data.get('titre')
            livre.annee_publication = data.get('annee_publication')
            livre.resume = data.get('resume')
            
            # --- Gestion des Auteurs (Relation Many-to-Many) ---
            # Dans le formulaire, l'auteur est transmis via une liste d'IDs
            selected_auteur_ids = request.form.getlist('auteurs')
            
            # Si c'est une édition, on efface l'ancienne relation pour la recréer
            if is_edit:
                livre.auteurs.clear() 
                db.session.commit() # Commit intermédiaire pour effacer les liens Ecrire
            
            # Recréation des liens
            for auth_id in selected_auteur_ids:
                auteur = Auteur.query.get(int(auth_id))
                if auteur:
                    livre.auteurs.append(auteur) # Utilise la relation back_populates

            if not is_edit:
                db.session.add(livre)
                flash(f"Livre '{livre.titre}' ajouté avec succès.", 'success')
            else:
                flash(f"Livre '{livre.titre}' mis à jour avec succès.", 'success')

            db.session.commit()
            return redirect(url_for('catalogue_bp.view_livre', isbn=livre.isbn))

        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de l'enregistrement du livre : {e}", 'danger')
            # Renvoie le formulaire avec les données soumises
            return render_template('catalogue/edit_livre.html', 
                                livre=livre, 
                                all_auteurs=all_auteurs,
                                is_edit=is_edit)

    # GET : Affichage du formulaire
    return render_template(
        'catalogue/edit_livre.html', 
        livre=livre, 
        all_auteurs=all_auteurs, 
        is_edit=is_edit,
        page_title='Modifier' if is_edit else 'Ajouter un Livre'
    )

# ... (Les routes pour l'ajout/modification/suppression des Exemplaires et des Auteurs sont nécessaires pour une gestion complète, mais ce contrôleur couvre la base.)