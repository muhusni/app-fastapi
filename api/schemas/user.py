from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Form

class UserCreate(BaseModel):
    username: Annotated[str, Form()]
    email: Annotated[EmailStr, Form()]
    name: Annotated[str, Form()]
    password: Annotated[str, Form()]

class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
