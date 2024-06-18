from fastapi import HTTPException, status


UserAlreadyExistsException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User already exists')
IncorrectEmailOrPwdException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect email or password')
TokenExpiredException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has expired')
TokenAbsentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token absent')
IncorrectTokenException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is incorrect')