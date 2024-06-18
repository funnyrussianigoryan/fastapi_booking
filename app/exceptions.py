from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class IncorrectEmailOrPwdException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect email or password'


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token has expired'


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token absent'


class IncorrectTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token is incorrect'
