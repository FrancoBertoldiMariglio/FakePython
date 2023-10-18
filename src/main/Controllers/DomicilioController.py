from fastapi import APIRouter

routerDomicilio = APIRouter()

@routerDomicilio.get("/api/v1/")
def getDomicilios():
    pass

@routerDomicilio.post("/api/v1/")
def postDomicilios():
    pass

@routerDomicilio.get("/api/v1/")
def putDomicilios():
    pass

@routerDomicilio.get("/api/v1/")
def deleteDomicilios():
    pass

@routerDomicilio.get("/api/v1/all")
def getAllDomicilios():
    pass