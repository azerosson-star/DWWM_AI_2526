from library_app.models.database import db
from datetime import date
from sqlalchemy.schema import UniqueConstraint # Utile pour les contraintes d'unicité

class Adherent(db.Model):
    """
    Modèle de la table 'adherent' qui gère les informations
    détaillées des membres autorisés à emprunter.
    """
    __tablename__ = 'adherent'

    # --- Attributs basés sur la BDD et l'Étude de cas ---

    # Clé primaire : Numéro d'adhérent
    num_adherent = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)

    # Adresse complète (Ajustement selon l'Étude de cas pour plus de détails)
    rue = db.Column(db.String(100))
    ville = db.Column(db.String(50))
    code_postal = db.Column(db.String(10))

    # Contact (Téléphone, l'email est géré par le User Model)
    telephone = db.Column(db.String(20))
    
    # Date d'adhésion (par défaut à la date de création)
    date_adhesion = db.Column(db.Date, default=date.today, nullable=False)

    # Clé étrangère vers la table 'users'
    # Cela établit la relation 1-à-1 entre un User authentifié et l'Adherent
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), unique=True, nullable=False)


    # --- Relations ---
    
    # Relation N-à-N via la table d'association 'emprunt'
    # Un Adhérent a plusieurs Emprunts (historique et actifs)
    emprunts = db.relationship('Emprunt', backref='adherent', lazy='dynamic')


    # --- Méthodes ---

    def __repr__(self):
        return f'<Adherent {self.num_adherent} - {self.prenom} {self.nom}>'

    def get_emprunts_actifs(self):
        """
        Méthode pour récupérer uniquement les emprunts non encore retournés.
        Utile pour la contrainte métier des 5 exemplaires maximum.
        """
        # Nécessite l'importation du modèle Emprunt si elle est dans un fichier séparé
        # from library_app.models.emprunt_model import Emprunt 
        # return Emprunt.query.filter(
        #     Emprunt.num_adherent == self.num_adherent,
        #     Emprunt.date_retour_effective.is_(None)
        # ).count()
        return self.emprunts.filter_by(date_retour_effective=None).count()

    # Méthode pour l'inscription (exemple de méthode statique)
    @staticmethod
    def create_adherent(user_id, nom, prenom, **kwargs):
        """ Crée un nouvel adhérent et le lie à un utilisateur existant. """
        new_adherent = Adherent(
            id_user=user_id,
            nom=nom,
            prenom=prenom,
            rue=kwargs.get('rue'),
            ville=kwargs.get('ville'),
            code_postal=kwargs.get('code_postal'),
            telephone=kwargs.get('telephone')
        )
        db.session.add(new_adherent)
        db.session.commit()
        return new_adherent