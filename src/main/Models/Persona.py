from src.main.Models.Base import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker

libros_personas = Table('libros_personas', Base.metadata,
                        Column('libro_id', Integer, ForeignKey('Libro.id')),
                        Column('persona_id', Integer, ForeignKey('Persona.id'))
                        )


class Persona(Base):
    __tablename__ = 'Persona'
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(Integer)
    domicilio_id = Column(Integer, ForeignKey('Domicilio.id'))

    domicilio = relationship('Domicilio', back_populates='personas', cascade="all, delete-orphan", lazy="joined")
    libros = relationship('Persona', secondary=libros_personas, back_populates='Libro', lazy="joined")
