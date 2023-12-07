from src.main.Models.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Domicilio(Base):

    __tablename__ = 'Domicilio'
    calle = Column(String)
    numero = Column(Integer)

    localidad_id = Column(Integer, ForeignKey('Localidad.id'))

    localidad = relationship('Localidad', back_populates='domicilios', lazy="joined")
    personas = relationship('Persona', back_populates='domicilio', lazy="joined")
