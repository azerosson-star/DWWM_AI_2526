from library_app.models.database import db # L'importation est ajustée pour la structure du package
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date # Nécessaire pour les dates

# La classe UserMixin de Flask-Login fournit les propriétés nécessaires 
# (is_authenticated, is_active, is_anonymous, get_id())
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    # --- Colonnes BDD (Basées sur library.sql) ---
    
    # Clé primaire (nommée id_user dans le SQL)
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Note : Le champ 'id' dans le modèle est remplacé par 'id_user' 
    # pour une meilleure correspondance avec le schéma SQL.
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Augmentation de la taille pour stocker un hash sécurisé (ex: scrypt)
    password = db.Column(db.String(256), nullable=False) 
    
    # Ajout des champs ROLE et CREATED_AT, présents dans library.sql 
    role = db.Column(db.Enum('user', 'admin'), default='user', nullable=False)
    created_at = db.Column(db.Date, default=date.today)
    
    # --- Relations ---
    # Relation 1-à-1 avec Adherent
    adherent = db.relationship('Adherent', backref='user', uselist=False, lazy=True)


# ==========================================================
    # MÉTHODES D'AUTHENTIFICATION ET DE GESTION DU CONTRÔLEUR
    # ==========================================================

    # 1. Méthode pour vérifier si l'email existe (User.email_exists)
    @classmethod
    def email_exists(cls, email):
        """Vérifie si un email existe déjà dans la base de données."""
        return cls.query.filter_by(email=email).first() is not None

    # 2. Méthode pour créer un nouvel utilisateur (User.create_user)
    @classmethod
    def create_user(cls, username, email, password, role='user'):
        """Crée et enregistre un nouvel utilisateur."""
        
        # Hachage du mot de passe pour la sécurité
        hashed_password = generate_password_hash(password)
        
        new_user = cls(
            username=username,
            email=email,
            password=hashed_password,
            role=role,
            created_at=date.today()
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            raise e

    # 3. Méthode pour authentifier l'utilisateur (User.authenticate)
    @classmethod
    def authenticate(cls, email, password):
        """Tente d'authentifier un utilisateur par email et mot de passe."""
        user = cls.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            return user
        return None

    # 4. Méthode pour charger l'utilisateur par ID (User.get)
    @classmethod
    def get(cls, user_id):
        """Récupère un utilisateur par son ID (utilisé par load_user)."""
        # Utiliser get() est plus rapide si la PK est connue
        return cls.query.get(int(user_id)) 

    # Implémentation du get_id requis par UserMixin
    def get_id(self):
        """Retourne l'identifiant unique de l'utilisateur (str)."""
        return str(self.id_user)

    def set_password(self, password):
        """Hache et stocke le mot de passe."""
        # Utilisation de la fonction generate_password_hash de Werkzeug
        # J'ai défini l'algorithme 'scrypt' dans le controller, mais ici on le laisse par défaut
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Vérifie le mot de passe haché."""
        return check_password_hash(self.password, password)

    # --- Méthode de Représentation ---

    def __repr__(self):
        return f'<User {self.email}, Role: {self.role}>'
    
    
# NOTE: La fonction load_user (nécessaire à Flask-Login) devra être définie 
# dans app.py ou dans __init__.py pour l'initialisation.