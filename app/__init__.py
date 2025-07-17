# app/__init__.py
from flask import Flask
from .routes.finca_route import bp_finca
from .modelo import crear_tablas

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_finca)
    crear_tablas()   # para SQLAlchemy: Base.metadata.create_all(engine)
    return app
