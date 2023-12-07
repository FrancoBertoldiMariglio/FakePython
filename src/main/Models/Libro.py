from src.main.Models.Base import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from .Persona import libros_personas

libros_autores = Table('libros_autores', Base.metadata,
                       Column('libro_id', Integer, ForeignKey('Libro.id')),
                       Column('autor_id', Integer, ForeignKey('Autor.id'))
                       )


class Libro(Base):
    __tablename__ = 'Libro'
    titulo = Column(String)
    fecha = Column(Integer)
    genero = Column(String)
    paginas = Column(Integer)

    autores = relationship('Autor', secondary=libros_autores, back_populates='Libro')
    personas = relationship('Persona', secondary=libros_personas, back_populates='Libro')
