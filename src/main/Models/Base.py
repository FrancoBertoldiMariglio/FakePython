from sqlalchemy import Column, Integer, String
from ..database import base


class Base(base):

    __abstract__ = True

    id = Column(Integer, primary_key = True)
