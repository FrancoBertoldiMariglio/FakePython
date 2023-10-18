from src.main.Entities.BaseEntity import BaseEntity
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Base
from sqlalchemy.orm import relationship, sessionmaker
from Persona import libros_personas

libros_autores = Table('libros_autores', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('autor_id', Integer, ForeignKey('autor.id'))
)

class Libro(BaseEntity):

    __tablename__ = 'Libro'
    titulo = Column(String)
    fecha = Column(Integer)
    genero = Column(String)
    paginas = Column(Integer)

    autores = relationship('Autor', secondary=libros_autores, back_populates='Libro')
    personas = relationship('Persona', secondary=libros_personas, back_populates='Libro')
