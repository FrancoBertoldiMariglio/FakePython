from fastapi import FastAPI
from .BaseController import BaseController
from ..Services.BaseServiceImp import BaseServiceImplement
from fastapi.responses import Response
from pydantic import BaseModel


class BaseControllerImplemt(BaseController):

    def __int__(self):
        self.service = BaseServiceImplement()

    def getAll(self):
        pass

    def getOne(self, id):
        pass
######

class Item(BaseModel):
    name: str
    price: float
    is_available: bool
    # Hay que añadir esto para manejar los datos

@app.post("/create_item")
def create_item(item: Item):
    return item
#######
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from mi_modelo import Base, Persona  # Asegúrate de importar tus modelos

app = FastAPI()

class PersonResponse(BaseModel):
    id: int
    nombre: str
    email: str

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@app.get("/personas", response_model=list[PersonResponse])
def get_personas():
    session = SessionLocal()
    personas = session.query(Persona).all()
    session.close()
    return personas