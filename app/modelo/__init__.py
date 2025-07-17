# app/modelo/__init__.py
"""Paquete de modelos ORM de SoFTgan."""

from .base import Base, crear_tablas 
from .finca import Finca
# Si en el futuro se añade: Usuario, Semoviente, etc:
# from .usuario import Usuario
# from .semoviente import Semoviente

__all__ = ["Base", "crear_tablas", "Finca"]
