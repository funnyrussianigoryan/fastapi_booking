from datetime import datetime

from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from app.config import settings
from app.exceptions import TokenExpiredException, TokenAbsentException, IncorrectTokenException
from app.users.service import UsersService


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.TOKEN_KEY, settings.TOKEN_ALG, )
    except JWTError:
        raise IncorrectTokenException
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get('sub')
    if not user_id:
        raise IncorrectTokenException
    user = await UsersService.get_by_id(int (user_id))
    if not user:
        raise IncorrectTokenException
    return user
