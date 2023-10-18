from src.main.Entities.BaseEntity import BaseEntity
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Base
from sqlalchemy.orm import relationship, sessionmaker

libros_personas = Table('libros_personas', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('persona_id', Integer, ForeignKey('persona.id'))
)

class Persona(BaseEntity):

    __tablename__ = 'Persona'
    nombre : Column(String)
    apellido = Column(String)
    dni = Column(Integer)
    domicilio_id = Column(Integer, ForeignKey('Domicilio.id'))

    domicilio = relationship('Domicilio', back_populates='Persona')
    libros = relationship('Persona', secondary=libros_personas, back_populates='Libro')