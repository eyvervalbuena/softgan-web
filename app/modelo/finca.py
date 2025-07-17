from sqlalchemy import Column, Integer, String, Float
from .base import Base   # IMPORTACIÓN RELATIVA CORRECTA

class Finca(Base):
    __tablename__ = 'finca'

    id_finca       = Column(Integer, primary_key=True)
    nombre         = Column(String(120), nullable=False)
    propietario    = Column(String(120), nullable=False)
    direccion      = Column(String(255))
    hectareas      = Column(Float)
    num_potreros   = Column(Integer)
    marca1         = Column(String(60), nullable=True)
    marca2         = Column(String(60), nullable=True)
    marca3         = Column(String(60), nullable=True)
    nit            = Column(String(60), nullable=True)
    email          = Column(String(120), nullable=True)
    tipo_ganado    = Column(String(60), nullable=True)
    edades_hembras = Column(String(120), nullable=True)
    edades_machos  = Column(String(120), nullable=True)
