from fastapi import APIRouter

routerAutores = APIRouter()

@routerAutores.get("/api/v1/")
def getAutoes():
    pass

@routerAutores.post("/api/v1/")
def postAutores():
    pass

@routerAutores.get("/api/v1/")
def putAutores():
    pass

@routerAutores.get("/api/v1/")
def deleteAutores():
    pass

@routerAutores.get("/api/v1/all")
def getAllAutores():
    pass