from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Form
from .employee import EmployeeResponse

class UserCreate(BaseModel):
    username: Annotated[str, Form()]
    nip: Annotated[str, Form()]
    name: Annotated[str, Form()]
    password: Annotated[str, Form()]

class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    NIP: str
    employee: EmployeeResponse | None

    class Config:
        from_attributes = True
