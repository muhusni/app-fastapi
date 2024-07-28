from typing import Annotated
from fastapi import Form, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.models import User, Employee
from database import get_db, get_db_sso
from api.utils import verify_password, create_jwt_token
from api.schemas import EmployeeResponse
from sqlalchemy.orm import joinedload
from api.utils.jwt_token_utils import add_to_blacklist

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
class AuthController:   
    @staticmethod 
    async def get_me(request: Request, ):
        user = getattr(request.state, "user", None)
        if user is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return {**request.state.state}
    
    @staticmethod 
    async def login(login: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db_sso)]):
        username = login.username
        password = login.password

        if username is None or password is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        user = db.query(User).options(joinedload(User.employee)).filter(User.username == username).first()

        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid username or password")
        employee_data = EmployeeResponse.model_validate(user.employee).model_dump() if user.employee else None
        data = {
            "sub": username,
            "nip": user.NIP,
            "name": user.name,
            "id": user.id,
            "employee": employee_data
        }

        # return data
        # Create JWT token
        token = create_jwt_token(data)
        return {"access_token": token, "token_type": "bearer"}

    async def logout(self, token: Annotated[str, Depends(oauth2_scheme)]):
        add_to_blacklist(token)
        return {"message": "User has logout"}