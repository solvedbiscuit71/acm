from fastapi import HTTPException
from pydantic import Field, BaseModel

from schema.database import get_waiter_hashed_password
from schema.security import validate_password


class Waiter(BaseModel):
    id: str = "waiter"
    password: str = Field(min_length=8)

async def authenticate_waiter(waiter_auth: Waiter):
    hashed_password = await get_waiter_hashed_password(waiter_auth.id)
    if validate_password(waiter_auth.password, hashed_password):
        return True
    else:
        raise HTTPException(status_code=401, detail="invalid password")
