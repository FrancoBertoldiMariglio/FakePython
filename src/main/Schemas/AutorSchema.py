from typing import Optional, List, TYPE_CHECKING

from pydantic import Field

from BaseSchema import BaseSchema


class AutorSchema(BaseSchema):
    nombre: Optional[str] = Field(alias='nombre')
    apellido: Optional[str] = Field(alias='apellido')
    biografia: Optional[str] = Field(alias='biografia')
