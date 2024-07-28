from fastapi import Request, HTTPException, Depends
from typing import Annotated
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
import jwt
import os
from api.utils.jwt_token_utils import is_token_blacklisted

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthBearer(HTTPBearer):
    async def __call__(self, request: Request, token: Annotated[str, Depends(oauth2_scheme)]):
        if is_token_blacklisted(token):
            raise HTTPException(status_code=401, detail="Token has expired")
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            token = credentials.credentials
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                user = payload.get("sub")
                if user is None:
                    raise HTTPException(status_code=401, detail="Invalid credentials")
                request.state.user = user
                request.state.id = payload.get("id")
                request.state.nip = payload.get("nip")
                request.state.name = payload.get("name")
                request.state.employee = payload.get("employee")
                
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="Token has expired")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=401, detail="Invalid token")
        else:
            raise HTTPException(status_code=401, detail="Invalid authorization code")
