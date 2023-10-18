from src.main.Entities.BaseEntity import BaseEntity
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

class Domicilio(BaseEntity):

    __tablename__ = 'Domicilio'
    calle = Column(String)
    numero = Column(Integer)
    localidad_id = Column(Integer, ForeignKey('Localidad.id'))

    localidad = relationship('Localidad', back_populates='Domicilio')
    persona = relationship('Persona', back_populates='Domicilio')
