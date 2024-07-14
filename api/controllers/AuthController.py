from typing import Annotated
from fastapi import Form, HTTPException

class AuthController:    
    async def get_me(): 
        return {"name" : "Me", "status" : "OK"}

    async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
        if username is None and password is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"username": username}