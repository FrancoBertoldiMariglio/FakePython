from fastapi import APIRouter

routerPersona = APIRouter()

@routerPersona.get("/api/v1/")
def getPersonas():
    pass

@routerPersona.post("/api/v1/")
def postPersonas():
    pass

@routerPersona.get("/api/v1/")
def putPersonas():
    pass

@routerPersona.get("/api/v1/")
def deletePersonas():
    pass

@routerPersona.get("/api/v1/all")
def getAllPersonas():
    pass