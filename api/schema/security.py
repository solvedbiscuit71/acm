import os
import dotenv

from fastapi import HTTPException
from bcrypt import hashpw, checkpw

from schema.waiter import Waiter
from schema.database import count_user_by_id, get_waiter_hashed_password, ObjectId

dotenv.load_dotenv()
salt = os.getenv('SALT').encode()


def hash_password(passwd: str) -> str:
    return hashpw(passwd.encode(), salt).decode()


def validate_password(passwd: str, hashed_passwd: str) -> bool:
    return checkpw(passwd.encode(), hashed_passwd.encode())


async def authenticate_id(id: ObjectId) -> ObjectId:
    if await count_user_by_id(id):
        return id
    else:
        raise HTTPException(status_code=400, detail="id not found")

async def authenticate_waiter(waiter_auth: Waiter):
    hashed_password = await get_waiter_hashed_password(waiter_auth.id)
    if validate_password(waiter_auth.password, hashed_password):
        return True
    else:
        raise HTTPException(status_code=401, detail="invalid password")
