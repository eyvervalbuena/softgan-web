# app/routes/main_route.py
from flask import Blueprint, redirect, url_for

bp_main = Blueprint('main', __name__)

@bp_main.route('/')
def index():
    # redirigimos a /finca/listar
    return redirect(url_for('finca.listar'))
