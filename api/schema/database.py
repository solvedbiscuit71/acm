from typing import Annotated
from fastapi import HTTPException, Depends
from pydantic import BaseModel
from bson.objectid import ObjectId as BaseObjectId
from bson.errors import InvalidId

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class ObjectId(BaseObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: str):
        try:
            return cls(value)
        except InvalidId:
            raise HTTPException(status_code=422, detail="invalid id")


class DBModel(BaseModel):
    class Config:
        json_encoders = {
            ObjectId: lambda value: str(value),
        }


class Connection:
    client: AsyncIOMotorClient = None


def database_connect():
    db.client = AsyncIOMotorClient()


def database_disconnect():
    db.client.close()


def get_database() -> AsyncIOMotorDatabase:
    return db.client["acm"]


async def get_user_by_id(id: ObjectId) -> dict:
    db = get_database()
    user = await db.users.find_one({"_id": id})
    if not user:
        raise HTTPException(status_code=400, detail="id not found")
    return user


async def get_user_by_mobile(mobile: str) -> dict:
    db = get_database()
    user = await db.users.find_one({"mobile": mobile})
    if not user:
        raise HTTPException(status_code=400, detail="mobile not found")
    return user


async def count_user_by_id(id: ObjectId) -> int:
    db = get_database()
    count = await db.users.count_documents({"_id": id})
    if not count:
        raise HTTPException(status_code=400, detail="id not found")
    return count


async def get_waiter_hashed_password(id: str) -> str:
    db = get_database()
    waiter = await db.waiter.find_one({"_id": id})
    if not waiter:
        raise HTTPException(status_code=500, detail="waiter not found")
    return waiter["hashed_password"]

db: Connection = Connection()
Database = Annotated[AsyncIOMotorDatabase, Depends(get_database)]
