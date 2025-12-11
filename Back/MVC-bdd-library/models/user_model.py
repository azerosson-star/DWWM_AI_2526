from models.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# La classe UserMixin de Flask-Login fournit les propriétés nécessaires 
# (is_authenticated, is_active, is_anonymous, get_id())
class User(db.Model, UserMixin):
    __tablename__ = 'users' # Nom de table distinct pour l'authentification

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        """Hache et stocke le mot de passe."""
        # Utilisation de la fonction generate_password_hash de Werkzeug
        self.password = generate_password_hash(password, method='scrypt')

    def check_password(self, password):
        """Vérifie le mot de passe haché."""
        return check_password_hash(self.password, password)

    @staticmethod
    def get(username):
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return f'<User {self.email}>'

# NOTE: La fonction load_user est définie dans app.py pour initialiser Flask-Login.

