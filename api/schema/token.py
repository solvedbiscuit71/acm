import os
import dotenv

from typing import Annotated
from fastapi import HTTPException, Header
from pydantic import BaseModel
from schema.user import UserId

from jwt import encode, decode
from jwt.exceptions import InvalidSignatureError, DecodeError

dotenv.load_dotenv()
secret = os.getenv('SECRET')
waiter_secret = os.getenv('WAITER_SECRET')
algorithm = os.getenv('ALGORITHM')


class Token(BaseModel):
    access_token: str
    type: str = "bearer"


class TokenData(UserId):
    pass


def create_access_token(payload: dict, type: str) -> str:
    match type:
        case 'access':
            return encode(payload=payload, key=secret, algorithm=algorithm)
        case 'waiter':
            return encode(payload=payload, key=waiter_secret, algorithm=algorithm)
        case _:
            raise HTTPException(status_code=500, detail="Invalid token type")

def validate_token(token: str, type: str) -> str:
    try:
        match type:
            case 'access':
                payload = decode(jwt=token, key=secret, algorithms=[algorithm])
            case 'waiter':
                payload = decode(jwt=token, key=waiter_secret, algorithms=[algorithm])
            case _:
                raise HTTPException(status_code=500, detail="Invalid token type")
        return payload["_id"]
    except InvalidSignatureError:
        raise HTTPException(status_code=401, detail="Invalid signature")
    except DecodeError:
        raise HTTPException(status_code=401, detail="Invalid signature")


def authenticate_access_token(authorization: Annotated[str, Header()]) -> str:
    type, token = authorization.split(' ')
    match type:
        case 'Bearer':
            return validate_token(token, 'access')
        case _:
            HTTPException(status_code=422, detail="Unsupported token")

def authenticate_waiter_token(authorization: Annotated[str, Header()]) -> str:
    type, token = authorization.split(' ')
    match type:
        case 'Bearer':
            return validate_token(token, 'waiter')
        case _:
            HTTPException(status_code=422, detail="Unsupported token")
