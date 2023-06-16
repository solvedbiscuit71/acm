from typing import Annotated

from fastapi import HTTPException, Header
from pydantic import Field
from pymongo.results import InsertOneResult, UpdateResult

from schema.database import ObjectId, DBModel, AsyncIOMotorDatabase, get_database, get_user_by_id, get_user_by_mobile
from schema.security import hash_password, validate_password 


class UserData(DBModel):
    name: str = "anonymous"
    mobile: str = Field(min_length=10, max_length=10, regex="^[0-9]*$")


class UserAuth(DBModel):
    id: ObjectId = Field(alias='_id')
    password: str = Field(min_length=8)


class UserDB(DBModel):
    id: ObjectId = Field(alias='_id')
    hashed_password: str


class UserCreate(UserData):
    password: str = Field(min_length=8)


class UserUpdate(DBModel):
    name: str = None
    mobile: str = Field(default=None, min_length=10,
                        max_length=10, regex="^[0-9]*$")
    password: str = Field(default=None, min_length=8)


class UserId(DBModel):
    id: ObjectId = Field(alias='_id')

async def create_user(user_data: UserCreate):
    db: AsyncIOMotorDatabase = get_database()

    payload = user_data.dict()
    payload.pop("password")
    payload.update({"hashed_password": hash_password(user_data.password)})

    count = await db.users.count_documents({"mobile": user_data.mobile})
    if count:
        raise HTTPException(status_code=409, detail="mobile already used")

    result: InsertOneResult = await db.users.insert_one(payload)
    return {"_id": result.inserted_id}

async def update_user(id, user_data: UserUpdate) -> tuple[int, int]:
    db: AsyncIOMotorDatabase = get_database()

    payload = dict()
    if user_data.name:
        payload.update({"name": user_data.name})

    if user_data.password:
        payload.update({"hashed_password": hash_password(user_data.password)})

    if user_data.mobile:
        count = await db.users.count_documents({"mobile": user_data.mobile,
                                                "_id": {"$ne": ObjectId(id)}})
        if count:
            raise HTTPException(status_code=409, detail="mobile already used")
        payload.update({"mobile": user_data.mobile})

    if payload:
        result: UpdateResult = await db.users.update_one({"_id": ObjectId(id)}, {"$set": payload})
        return (result.matched_count, result.modified_count)
    else:
        return (0, 0)

async def authenticate_user_id(user_auth: UserAuth) -> ObjectId:
    user = await get_user_by_id(user_auth.id)
    if validate_password(user_auth.password, user["hashed_password"]):
        return user["_id"]
    else:
        raise HTTPException(status_code=401, detail="invalid password")


async def authenticate_user_mobile(mobile: Annotated[str, Header()], password: Annotated[str, Header()]) -> ObjectId:
    user = await get_user_by_mobile(mobile)
    if validate_password(password, user["hashed_password"]):
        return user["_id"]
    else:
        raise HTTPException(status_code=401, detail="invalid password")
