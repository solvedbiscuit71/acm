from pydantic import BaseModel
from schema.user import UserOut


class Token(BaseModel):
    access_token: str
    type: str = "bearer"


class TokenData(UserOut):
    pass
