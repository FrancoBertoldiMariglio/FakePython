from src.main.Entities.BaseEntity import BaseEntity
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

class Localidad(BaseEntity):

    __tablename__ = 'Localidad'
    denominacion = Column(String)

    domicilios = relationship('Domicilio', back_populates='localidad')
