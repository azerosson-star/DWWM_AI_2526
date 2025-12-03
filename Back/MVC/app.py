from flask import Flask
from controllers.main_controller import MainController

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

@app.route('/')
def index():
    return MainController.index()

if __name__ == '__main__':
    app.run(debug=True)