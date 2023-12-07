from typing import Optional, List, TYPE_CHECKING

from pydantic import Field

from BaseSchema import BaseSchema


class DomicilioSchema(BaseSchema):
    calle: Optional[str] = Field(alias='calle')
    numero = Optional[int] = Field(alias='numero')

    localidad_id: Optional[int] = Field(alias='localidad_id')
