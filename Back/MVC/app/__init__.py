from flask import Flask

app = Flask(__name__)

from app.controllers import main_controller

app.register_blueprint(main_controller.bp)