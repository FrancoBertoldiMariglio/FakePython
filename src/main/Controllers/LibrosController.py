from fastapi import APIRouter

routerLibro = APIRouter()

@routerLibro.get("/api/v1/")
def getLibros():
    pass

@routerLibro.post("/api/v1/")
def postLibros():
    pass

@routerLibro.get("/api/v1/")
def putLibros():
    pass

@routerLibro.get("/api/v1/")
def deleteLibros():
    pass

@routerLibro.get("/api/v1/all")
def getAllLibros():
    pass