# Modèle Adherent (Table 'adherent')
from app.models.database import db

class Adherent(db.Model):
    __tablename__ = 'adherent'

    # Correspond à la colonne num_adherent (PK)
    num_adherent = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    adresse = db.Column(db.String(50))
    date_adhesion = db.Column(db.String(50)) # Type VARCHAR/String selon le SQL fourni

    # Relation 1-N: Un Adhérent peut avoir plusieurs Emprunts
    emprunts = db.relationship('Emprunter', backref='adherent', lazy=True)

    def __repr__(self):
        return f"Adherent('{self.nom}', '{self.prenom}')"