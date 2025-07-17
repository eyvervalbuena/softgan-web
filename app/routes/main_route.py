from flask import Blueprint, redirect, url_for

bp_main = Blueprint('main', __name__)

@bp_main.route('/')
def index():
    # redirige a finca lista
    return redirect(url_for('finca.listar'))
