from typing import Optional, List, TYPE_CHECKING

from pydantic import Field

from BaseSchema import BaseSchema


class LibroSchema(BaseSchema):
    titulo: Optional[str] = Field(alias='titulo')
    fecha: Optional[int] = Field(alias='fecha')
    genero: Optional[str] = Field(alias='genero')
    paginas: Optional[int] = Field(alias='paginas')
