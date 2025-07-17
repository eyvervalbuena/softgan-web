
from flask import Flask
from .routes.main_route import bp_main
from .routes.finca_route import bp_finca
from .modelo import crear_tablas

def create_app():
    app = Flask(__name__)


    app.secret_key = "Adso2977369" # cambiar la clave
    
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_finca)

    crear_tablas() 
    return app
