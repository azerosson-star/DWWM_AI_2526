from flask import jsonify, render_template, request, redirect, url_for, session, flash
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import text

from config import db, Config

import os

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"

    def set_password(self, password: str):
        """Définit le mot de passe de l'utilisateur (hashé)."""
        self.password = UserController.hash_password(password)

    @staticmethod
    def check_password(stored_password: str, provided_password: str) -> bool:
        # Extraire le sel et le mot de passe haché du mot de passe stocké
        salt_hex = stored_password[:32]
        stored_hashed_password_hex = stored_password[32:]

        salt = bytes.fromhex(salt_hex)
        stored_hashed_password = bytes.fromhex(stored_hashed_password_hex)

        # Utiliser PBKDF2 pour hacher le mot de passe fourni
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        provided_hashed_password = kdf.derive(provided_password.encode())

        # Comparer les mots de passe hachés
        return provided_hashed_password == stored_hashed_password

class UserController:
    @staticmethod
    def register():
        """Endpoint d'exemple pour insérer un utililisateur dans la table `users`.
        Corps JSON attendu: {"username": "...", "email": "..."}
        """
        if request.method == 'POST':
            
            data = request.form
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username or not email or not password:
                return jsonify({'error': 'All fields are required'}), 400

            user = User(username=username, email=email)
            user.set_password(password)

            try:
                db.session.add(user)
                db.session.commit()
                flash('Registration successful!', 'success')
                return redirect(url_for('index'))
                #return jsonify({'id': user.id, 'username': user.username, 'password': user.password, 'email': user.email}), 201
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': str(e)}), 500
        else:
            return render_template('register.html')

    @staticmethod
    def login():
        if request.method == 'POST':    
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter_by(username=username).first()

            if user and User.check_password(user.password, password):
                # Définir la session utilisateur
                session['username'] = username
                
                flash('Connexion réussie!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Username ou mot de passe incorrect.', 'danger')

        return render_template('login.html')

    @staticmethod
    def hash_password(password: str) -> str:
        # Générer un sel aléatoire
        salt = os.urandom(16)

        # Utiliser PBKDF2 pour hacher le mot de passe
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        hashed_password = kdf.derive(password.encode())

        # Retourner le sel et le mot de passe haché sous forme de chaîne hexadécimale
        return salt.hex() + hashed_password.hex()