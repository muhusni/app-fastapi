from typing import Annotated
from fastapi import Form, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.schemas import LoginRequest
from sqlalchemy.orm import Session
from api.models import User
from database import get_db
from utils import verify_password, create_jwt_token

class AuthController:   
    @staticmethod 
    async def get_me(request: Request, ):
        user = getattr(request.state, "user", None)
        if user is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return {**request.state._state}
    
    @staticmethod 
    async def login(login: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]):
        username = login.username
        password = login.password

        if username is None or password is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        user = db.query(User).filter(User.username == username).first()
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid username or password")
        data = {
            "sub": username,
            "email": user.email,
            "name": user.name,
            "id": user.id
        }

        # Create JWT token
        token = create_jwt_token(data)
        return {"access_token": token, "token_type": "bearer"}