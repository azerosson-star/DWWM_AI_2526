import os

class Config:   
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre_cle_secrete_tres_sure'
    
    user = os.getenv('MYSQL_USER', 'root')
    password = os.getenv('MYSQL_ROOT_PASSWORD', 'root_password')
    host = os.getenv('MYSQL_HOST', 'localhost')
    port = os.getenv('MYSQL_PORT', '6033')
    db = os.getenv('MYSQL_DB', 'library')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
