from fastapi import APIRouter

routerLocalidad = APIRouter()

@routerLocalidad.get("/api/v1/")
def getLocalidad():
    pass

@routerLocalidad.post("/api/v1/")
def postLocalidads():
    pass

@routerLocalidad.get("/api/v1/")
def putLocalidads():
    pass

@routerLocalidad.get("/api/v1/")
def deleteLocalidads():
    pass

@routerLocalidad.get("/api/v1/all")
def getAllLocalidads():
    pass