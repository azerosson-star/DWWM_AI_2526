from flask import Flask
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from models.user_model import User


# Crée une instance de Blueprint.
# Le préfixe d'URL ('/') signifie que les routes définies ici
# ne nécessitent pas de préfixe supplémentaire (ex: /login, /register).
user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # A faire
    return render_template('login.html')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    # A faire

    return render_template('register.html')

@user_bp.route('/logout')
def logout():
    logout_user()
    flash('Déconnexion réussie!', 'success')
    return redirect(url_for('main.index'))