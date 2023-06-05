from fastapi import HTTPException
from pydantic import BaseModel
from bson.objectid import ObjectId as BaseObjectId

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class ObjectId(BaseObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: str):
        try:
            return cls(value)
        except:
            raise ValueError("Not a valid ObjectId")


class DBModel(BaseModel):
    class Config:
        json_encoders = {
            ObjectId: lambda value: str(value),
        }


class Database:
    client: AsyncIOMotorClient = None


db: Database = Database()


def database_connect():
    db.client = AsyncIOMotorClient()


def database_disconnect():
    db.client.close()


def get_database() -> AsyncIOMotorDatabase:
    return db.client["acm"]


async def get_user(id: ObjectId) -> dict:
    db = get_database()
    user = await db.users.find_one({"_id": id})
    if not user:
        raise HTTPException(status_code=400, detail="id not found")
    return user


async def count_user_by_id(id: ObjectId) -> int:
    db = get_database()
    count = await db.users.count_documents({"_id": id})
    if not count:
        raise HTTPException(status_code=400, detail="id not found")
    return count
