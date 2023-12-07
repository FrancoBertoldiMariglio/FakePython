from pydantic import Optional, List, TYPE_CHECKING, Field


class PersonaLibroSchema():
    persona_id: Optional[int] = Field(alias='persona_id')
    libro_id: Optional[int] = Field(alias='libro_id')
