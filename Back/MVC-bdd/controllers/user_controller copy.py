from flask import Flask, jsonify, render_template, request, redirect, url_for, flash

class UserController:
    @staticmethod
    def register():
        if request.method == 'POST':
            # Logique d'inscription ici
            return redirect(url_for('login'))
        return render_template('register.html')

    @staticmethod
    def login():
        if request.method == 'POST':
            # Logique de connexion ici
            return redirect(url_for('index'))
        return render_template('login.html')
