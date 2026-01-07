from library_app.models.database import db
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

class Exemplaire(db.Model):
    """
    Modèle de la table 'exemplaire', représentant une copie physique d'un Livre.
    """
    __tablename__ = 'exemplaire'

    # --- Attributs basés sur la BDD et l'Étude de cas ---

    # Clé primaire : Numéro d'inventaire unique pour chaque copie
    num_inventaire = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Clé étrangère vers l'oeuvre (Livre)
    isbn = db.Column(db.String(17), db.ForeignKey('livre.isbn'), nullable=False)

    # Type d'utilisation : Vente ou Prêt (selon l'étude de cas)
    # Utilisation de db.Enum pour forcer la valeur à l'une de ces options
    type_usage = db.Column(Enum('vente', 'prêt', name='usage_types'), nullable=False)

    # --- Relations ---
    
    # Relation One-to-Many vers Emprunt
    # Un Exemplaire peut avoir plusieurs Emprunts (historique des prêts)
    # 'lazy=dynamic' est utilisé ici car nous aurons souvent besoin de requêtes filtrées 
    # pour vérifier si l'exemplaire est actuellement emprunté.
    emprunts = db.relationship('Emprunt', backref='exemplaire', lazy='dynamic')


    # --- Méthodes ---

    def __repr__(self):
        return f'<Exemplaire N°{self.num_inventaire} - ISBN:{self.isbn}, Usage:{self.type_usage}>'

    def is_disponible_au_pret(self):
        """
        Vérifie si l'exemplaire est disponible pour un nouveau prêt.
        Conditions :
        1. type_usage doit être 'prêt'.
        2. Il ne doit pas y avoir d'emprunt actif (date_retour_effective est NULL).
        """
        if self.type_usage != 'prêt':
            return False # Non disponible s'il est destiné à la vente

        # On vérifie si un emprunt est en cours (sans date de retour effective)
        # Nécessite l'importation du modèle Emprunt (généralement fait dans emprunt_model.py)
        
        # Le 'lazy=dynamic' sur la relation 'emprunts' permet cette requête efficace
        emprunt_actif = self.emprunts.filter_by(date_retour_effective=None).first()
        
        return emprunt_actif is None

    def get_statut(self):
        """Retourne le statut actuel de l'exemplaire."""
        if self.type_usage == 'vente':
            return 'En Vente'
        
        if self.is_disponible_au_pret():
            return 'Disponible au Prêt'
        
        return 'Actuellement Emprunté'