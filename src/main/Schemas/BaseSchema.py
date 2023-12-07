from typing import Optional
from pydantic import BaseModel, Field


class BaseSchema(BaseModel):

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        orm_mode = True

    id: Optional[int] = Field(alias='id')
