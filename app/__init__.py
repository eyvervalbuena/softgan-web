# app/__init__.py
from flask import Flask
from .routes.finca_route import bp_finca
from .routes.main_route  import bp_main
from .modelo             import crear_tablas

def create_app():
    app = Flask(__name__, static_folder="../statics", template_folder="templates")
    app.register_blueprint(bp_main)     # <<=== La ruta raíz
    app.register_blueprint(bp_finca)    # <<=== Tu módulo de fincas
    crear_tablas()
    return app
