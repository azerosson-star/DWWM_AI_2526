from flask import render_template

class MainController:
    @staticmethod
    def index():
        return render_template('index.html')