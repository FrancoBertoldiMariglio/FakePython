from fastapi import FastAPI
from .Controllers import AutoresController
from .Controllers import DomicilioController
from .Controllers import LibrosController
from .Controllers import LocalidadController
from .Controllers import PersonaController
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import uvicorn

#app = FastAPI()
#@app.get("/")

def main():

    app = FastAPI()

    app.include_router(AutoresController.routerAutores, prefix="/autores", tags=["autores"])
    app.include_router(DomicilioController.routerDomicilio, prefix="/domicilio", tags=["domicilios"])
    app.include_router(LibrosController.routerLibro, prefix="/libro", tags=["libros"])
    app.include_router(LocalidadController.routerLocalidad, prefix="/localidad", tags=["localidad"])
    app.include_router(PersonaController.routerPersona, prefix="/personas", tags=["personas"])

    DATABASE_URL = "sqlite:///./test.db"

    if not os.path.exists("./test.db"):
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    uvicorn.run(app, host="127.0.0.1", port=8000)

# uvicorn main:app --reload


if __name__ == "__main__":
    main()