import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

class Config:
    @staticmethod
    def get_database_uri() -> str:     
        user = os.getenv('MYSQL_USER', 'root')
        password = os.getenv('MYSQL_ROOT_PASSWORD', 'root_password')
        host = os.getenv('MYSQL_HOST', 'localhost')
        port = os.getenv('MYSQL_PORT', '6033')
        db = os.getenv('MYSQL_DB', 'myapp')

        # Encodage du mot de passe au besoin
        password = quote_plus(password)

        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"

    def init_app(app: Flask):
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.get_database_uri()
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
