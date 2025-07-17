from sqlalchemy.orm import declarative_base
from config import engine, SessionLocal

Base = declarative_base()

def crear_tablas():
    Base.metadata.create_all(bind=engine)

