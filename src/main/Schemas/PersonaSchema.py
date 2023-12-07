from typing import Optional, List, TYPE_CHECKING

from pydantic import Field

from BaseSchema import BaseSchema


class PersonaSchema(BaseSchema):
    nombre: Optional[str] = Field(alias='nombre')
    apellido = Optional[str] = Field(alias='apellido')
    dni = Optional[int] = Field(alias='dni')

    domicilio_id: Optional[int] = Field(alias='domicilio_id')
