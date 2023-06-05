import os
import dotenv

from fastapi import HTTPException
from bcrypt import hashpw, checkpw

from schema.user import UserAuth
from schema.database import get_user_by_id, count_user_by_id, ObjectId

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


async def authenticate_user(user_auth: UserAuth) -> ObjectId:
    user = await get_user_by_id(user_auth.id)
    if validate_password(user_auth.password, user["hashed_password"]):
        return user["_id"]
    else:
        raise HTTPException(status_code=401, detail="Invalid password")
