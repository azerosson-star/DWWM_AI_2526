from flask import Blueprint, render_template

bp = Blueprint('main', __name__, template_folder='../views/templates')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')