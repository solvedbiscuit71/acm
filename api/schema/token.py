from pydantic import BaseModel
from schema.user import UserId


class Token(BaseModel):
    access_token: str
    type: str = "bearer"


class TokenData(UserId):
    pass
