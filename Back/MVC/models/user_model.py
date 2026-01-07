from app import app
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize the app with the database
app.config['SQLALCHEMY_DATABASE_URI'] = Config.get_database_uri()

# Initialize SQLAlchemy without app
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


