from src.main.Models.Base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Localidad(Base):

    __tablename__ = 'Localidad'
    denominacion = Column(String)

    domicilios = relationship('Domicilio', back_populates='localidad', lazy="joined")
