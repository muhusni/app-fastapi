from fastapi import HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from api.models import User
from api.schemas.user import UserCreate, UserResponse
from database import get_db_sso
from api.utils import hash_password

class UserController:
    def create_user(self, user: UserCreate, db: Annotated[Session, Depends(get_db_sso)]):
        db_user = db.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        new_user = User(
            username = user.username,
            NIP = user.nip,
            name = user.name,
            password = hash_password(user.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_user(self, user_id: int, db: Annotated[Session, Depends(get_db_sso)]) -> UserResponse:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
