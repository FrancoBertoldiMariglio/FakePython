from .Controllers import AutoresController
from .Controllers import DomicilioController
from .Controllers import LibrosController
from .Controllers import LocalidadController
from .Controllers import PersonaController
from fastapi import FastAPI
import os
import uvicorn
from .database import SessionLocal, engine
from .Models import Base


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def main():
    app = FastAPI()
    Base.base.metadata.create_all(bind=engine)

    app.include_router(AutoresController.routerAutores, prefix="/autores", tags=["autores"])
    app.include_router(DomicilioController.routerDomicilio, prefix="/domicilio", tags=["domicilios"])
    app.include_router(LibrosController.routerLibro, prefix="/libro", tags=["libros"])
    app.include_router(LocalidadController.routerLocalidad, prefix="/localidad", tags=["localidad"])
    app.include_router(PersonaController.routerPersona, prefix="/personas", tags=["personas"])

    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
