from abc import abstractmethod, ABC
from ..Schemas.BaseSchema import BaseSchema
from ..Models import Base


class BaseRepository(ABC):

    @abstractmethod
    def findById(self, id: int) -> BaseSchema:
        """Devuelve un registro por ID"""

    @abstractmethod
    def findAll(self) -> list[BaseSchema]:
        """Devuelve todos los registros"""

    @abstractmethod
    def save(self, object: BaseSchema) -> BaseSchema:
        """Guarda un registro"""

    @abstractmethod
    def update(self, id: int, object: BaseSchema) -> BaseSchema:
        """Actualiza un registro"""

    @abstractmethod
    def delete(self, id: int) -> None:
        """Elimina un registro"""


