from ..Schemas.BaseSchema import BaseSchema
from sqlalchemy.orm import Session
from ..Models.Base import Base


class BaseRepository:
    def __init__(self, database_url):
        self.db = Session

    def findById(self, id: int) -> BaseSchema:
        """Devuelve un registro por ID"""


    def findAll(self) -> list[BaseSchema]:
        return self.db.query(Base).all()


    def save(self, object: BaseSchema) -> BaseSchema:
        """Guarda un registro"""


    def update(self,id: int, object: BaseSchema) -> BaseSchema:
        """Actualiza un registro"""


    def delete(self, id: int) -> None:
        """Elimina un registro"""

