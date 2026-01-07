from library_app.models.database import db
from sqlalchemy.orm import relationship, backref # Importation pour les relations

# --- Table d'Association (Écrire) ---

# Cette classe représente la table de liaison Many-to-Many entre Livre et Auteur.
class Ecrire(db.Model):
    __tablename__ = 'ecrire'

    # Clé primaire composée des clés étrangères
    isbn = db.Column(db.String(17), db.ForeignKey('livre.isbn'), primary_key=True)
    id_auteur = db.Column(db.Integer, db.ForeignKey('auteur.id_auteur'), primary_key=True)

    # Relations (Optionnel, mais utile pour accéder aux objets parents)
    livre = relationship("Livre", backref=backref("ecritures", cascade="all, delete-orphan"))
    auteur = relationship("Auteur", backref=backref("ecritures", cascade="all, delete-orphan"))


# --- Modèle Auteur ---

class Auteur(db.Model):
    """
    Modèle de la table 'auteur'.
    """
    __tablename__ = 'auteur'

    id_auteur = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    
    # Année de naissance (Optionnel, selon l'étude de cas)
    # annee_naissance = db.Column(db.Integer, nullable=True)

    # Relation Many-to-Many vers Livre
    # 'secondary' pointe vers la table d'association 'Ecrire'
    livres = relationship('Livre', secondary='ecrire', back_populates='auteurs')

    def __repr__(self):
        return f'<Auteur {self.nom} {self.prenom}>'


# --- Modèle Livre ---

class Livre(db.Model):
    """
    Modèle de la table 'livre' (l'œuvre).
    """
    __tablename__ = 'livre'

    # Clé primaire : ISBN (identifiant unique de l'œuvre)
    isbn = db.Column(db.String(17), primary_key=True) # VARCHAR(17) pour couvrir les formats ISBN-13 avec tirets

    titre = db.Column(db.String(255), nullable=False)
    annee_publication = db.Column(db.Integer)
    resume = db.Column(db.Text)

    # --- Relations ---

    # Relation Many-to-Many vers Auteur
    # 'secondary' pointe vers la table d'association 'Ecrire'
    # livres = relationship('Livre', secondary='ecrire', back_populates='auteurs')
    auteurs = relationship('Auteur', secondary='ecrire', back_populates='livres')

    # Relation One-to-Many vers Exemplaire (Une œuvre a plusieurs copies physiques)
    exemplaires = relationship('Exemplaire', backref='livre', lazy='dynamic')


    # --- Méthodes ---

    def __repr__(self):
        return f'<Livre ISBN:{self.isbn} - {self.titre}>'