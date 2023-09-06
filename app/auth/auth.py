from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()

def authentica_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "username"
    correct_password = "password"
    
    if credentials.username == correct_username and credentials.password == correct_password: 
        return True
    raise HTTPException(status_code=401, detail="Credenciales invalidas")
