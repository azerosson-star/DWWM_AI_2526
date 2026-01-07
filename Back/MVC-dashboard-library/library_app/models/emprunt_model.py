from library_app.models.database import db
from datetime import date, timedelta # Nécessaire pour gérer les dates et la durée de prêt

class Emprunt(db.Model):
    """
    Modèle de la table 'emprunt'. C'est la table d'association
    qui enregistre les prêts entre un Adhérent et un Exemplaire.
    """
    __tablename__ = 'emprunt'
    
    # --- Contraintes Métier Fixes (selon l'étude de cas) ---
    DUREE_PRET_JOURS = 21

    # --- Attributs basés sur la BDD ---

    # Clé primaire : ID auto-incrémenté pour identifier l'occurrence du prêt
    id_emprunt = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Clé étrangère vers l'Adhérent
    num_adherent = db.Column(db.Integer, db.ForeignKey('adherent.num_adherent'), nullable=False)
    
    # Clé étrangère vers l'Exemplaire
    num_inventaire = db.Column(db.Integer, db.ForeignKey('exemplaire.num_inventaire'), nullable=False)

    # Date de l'emprunt (automatiquement enregistrée à la création)
    date_emprunt = db.Column(db.Date, default=date.today, nullable=False)
    
    # Date de retour prévue (Calculée automatiquement selon la règle des 21 jours)
    # Note: La valeur par défaut est calculée dynamiquement.
    date_retour_prevue = db.Column(db.Date, nullable=False)
    
    # Date de retour effective (NULL si l'exemplaire n'est pas encore rendu)
    date_retour_effective = db.Column(db.Date, nullable=True)

    # Contrainte unique sur le couple (num_inventaire, date_retour_effective=NULL) est
    # gérée au niveau de la logique métier du Contrôleur (pour s'assurer qu'un exemplaire
    # n'a qu'un seul prêt actif).
    
    
    # --- Relations (déjà définies dans les modèles parents, ici pour complétude) ---
    # adherent (backref dans Adherent_model)
    # exemplaire (backref dans Exemplaire_model)
    
    # --- Constructeur et Logique Métier ---

    def __init__(self, num_adherent, num_inventaire, **kwargs):
        """
        Initialiseur qui calcule automatiquement la date de retour prévue.
        """
        super().__init__(num_adherent=num_adherent, num_inventaire=num_inventaire, **kwargs)
        
        # Calcul de la date de retour prévue
        if self.date_emprunt:
            self.date_retour_prevue = self.date_emprunt + timedelta(days=self.DUREE_PRET_JOURS)
        else:
            # Si date_emprunt n'est pas fourni (utilise date.today par défaut)
            self.date_retour_prevue = date.today() + timedelta(days=self.DUREE_PRET_JOURS)


    # --- Méthodes ---

    def est_en_cours(self):
        """
        Vérifie si l'emprunt est actif (l'exemplaire n'a pas été rendu).
        """
        return self.date_retour_effective is None

    def est_en_retard(self):
        """
        Vérifie si l'emprunt est en retard par rapport à la date de retour prévue.
        """
        if self.est_en_cours():
            return date.today() > self.date_retour_prevue
        return False # Pas en retard si déjà rendu

    def enregistrer_retour(self):
        """
        Enregistre la date de retour effective (date du jour).
        Cette méthode sera appelée par le pret_controller lors du retour.
        """
        if self.est_en_cours():
            self.date_retour_effective = date.today()
            return True
        return False

    def __repr__(self):
        statut = "Actif" if self.est_en_cours() else "Terminé"
        return f'<Emprunt {self.id_emprunt} - Adh:{self.num_adherent}, Exp:{self.num_inventaire}, Statut:{statut}>'