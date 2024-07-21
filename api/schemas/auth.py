from pydantic import BaseModel, EmailStr
# from typing import Annotated
# from fastapi import Form

class LoginRequest(BaseModel):
    username: str
    password: str