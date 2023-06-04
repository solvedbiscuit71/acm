from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles

from pymongo.results import InsertOneResult, UpdateResult
from motor.motor_asyncio import AsyncIOMotorDatabase

from schema.item import Item
from schema.user import UserIn, UserInOptional, UserOut
from schema.database import get_database, database_connect, database_disconnect, ObjectId, validate_id

app = FastAPI()

Database = Annotated[AsyncIOMotorDatabase, Depends(get_database)]
Id = Annotated[ObjectId, Depends(validate_id)]


@app.post("/user", response_model=UserOut)
async def create_user(user_data: UserIn, db: Database):
    payload = user_data.dict()
    payload.pop("password")
    payload.update({"hashed_password": "xxx"})

    count = await db.users.count_documents({"mobile": user_data.mobile})
    if count:
        raise HTTPException(status_code=409, detail="mobile already used")

    result: InsertOneResult = await db.users.insert_one(payload)
    payload.pop("hashed_password")
    payload.update({"_id": result.inserted_id})

    return payload


@app.patch("/user/{id}", response_model=None)
async def create_user(id: Id, user_data: UserInOptional, db: Database):
    payload = {}
    if user_data.name is not None:
        payload.update({"name": user_data.name})

    if user_data.password is not None:
        payload.update({"hashed_password": "xxx"})

    if user_data.mobile is not None:
        count = await db.users.count_documents({"mobile": user_data.mobile,
                                                "_id": {"$ne": id}})
        if count:
            raise HTTPException(status_code=409, detail="mobile already used")
        payload.update({"mobile": user_data.mobile})

    if payload:
        result: UpdateResult = await db.users.update_one({"_id": id}, {"$set": payload})
        return {"message": "success", "modified_count": result.modified_count}
    else:
        return {"message": "success", "modified_count": 0}


@app.get("/menu", response_model=list[Item])
async def menu(db: Database):
    items = []
    async for item in db.items.find():
        items.append(item)

    return items


app.mount('/image', StaticFiles(directory="image"), name="image")

app.add_event_handler("startup", database_connect)
app.add_event_handler("shutdown", database_disconnect)
