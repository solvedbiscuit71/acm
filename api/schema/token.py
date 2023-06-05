import os
import dotenv

from typing import Annotated
from fastapi import HTTPException, Header
from pydantic import BaseModel
from schema.user import UserId
from schema.database import ObjectId

from jwt import encode, decode
from jwt.exceptions import InvalidSignatureError

dotenv.load_dotenv()
secret = os.getenv('SECRET')
algorithm = os.getenv('ALGORITHM')


class Token(BaseModel):
    access_token: str
    type: str = "bearer"


class TokenData(UserId):
    pass


def create_access_token(payload: dict) -> str:
    return encode(payload=payload, key=secret, algorithm=algorithm)


def validate_token(token: str) -> ObjectId:
    try:
        payload = decode(jwt=token, key=secret, algorithms=[algorithm])
        return ObjectId(payload["_id"])
    except InvalidSignatureError:
        raise HTTPException(status_code=401, detail="Invalid signature")


def authenticate_token(authorization: Annotated[str, Header()]) -> ObjectId:
    type, token = authorization.split(' ')
    match type:
        case 'Bearer':
            return validate_token(token)
        case _:
            HTTPException(status_code=422, detail="Unsupported token")
