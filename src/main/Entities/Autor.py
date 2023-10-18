from src.main.Entities.BaseEntity import BaseEntity
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from Libro import libros_autores

class Autor(BaseEntity):
    __tablename__ = 'Autor'
    nombre = Column(String)
    apellido = Column(String)
    biografia = Column(String)
    libros = relationship('Libro', secondary=libros_autores, back_populates='Autor')
