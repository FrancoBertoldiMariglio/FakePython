from pydantic import Optional, List, TYPE_CHECKING, Field


class AutorLibroSchema():
    autor_id: Optional[int] = Field(alias='autor_id')
    libro_id: Optional[int] = Field(alias='libro_id')
