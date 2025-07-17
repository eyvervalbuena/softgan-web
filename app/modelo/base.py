from sqlalchemy.orm import declarative_base
from ..config import engine

Base = declarative_base()

def crear_tablas():
    """Crea todas las tablas registradas en Base."""
    print("Creando tablas...")
    Base.metadata.create_all(engine)
    print("Tablas creadas correctamente.")
