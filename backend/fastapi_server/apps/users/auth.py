from typing import Annotated
from fastapi import Cookie, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .core import validate_access_token
from .schemas import ActiveUser
from .settings import SETTINGS

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)


async def with_active_user(
    token: str = Depends(oauth2_scheme),
    auth: Annotated[str | None, Cookie()] = None,
) -> ActiveUser:
    access_token = token
    if SETTINGS["ACCESS_TOKEN_VIA_COOKIE"]:
        access_token = auth if auth else token
    try:
        user_data = await validate_access_token(access_token)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return ActiveUser(**user_data)
