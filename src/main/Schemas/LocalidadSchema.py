from typing import Optional, List, TYPE_CHECKING

from pydantic import Field

from BaseSchema import BaseSchema


class LocacalidadSchema(BaseSchema):
    denominacion: Optional[str] = Field(alias='denominacion')
