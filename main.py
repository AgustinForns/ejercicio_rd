from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from config.database import Session, Base, engine
from models.item import Item
from schemas.item import ItemSchema
from router.router import router

security = HTTPBasic()

def authentica_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "usuario"
    correct_password = "contraseña"
    
    if credentials.username == correct_username and credentials.password == correct_password: 
        return True
    return False

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
 
    
''' @app.middleware("http")
async def basic_auth_middleware(request: Request, call_next):
    if not await authentica_user(request):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    response =  await call_next(request)
    return response '''
