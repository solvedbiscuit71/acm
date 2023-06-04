from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles

from pymongo.results import InsertOneResult
from motor.motor_asyncio import AsyncIOMotorDatabase

from schema.item import Item
from schema.user import UserIn, UserOut
from schema.database import get_database, database_connect, database_disconnect

app = FastAPI()

Database = Annotated[AsyncIOMotorDatabase, Depends(get_database)]


@app.post("/user", response_model=UserOut)
async def create_user(user_data: UserIn, db: Database):
    payload = user_data.dict()
    payload.pop("password")
    payload.update({"hashed_password": "xxx"})

    result = await db.users.find_one({"mobile": user_data.mobile})
    if result is not None:
        raise HTTPException(status_code=409, detail="mobile already used")

    result: InsertOneResult = await db.users.insert_one(payload)
    payload.pop("hashed_password")
    payload.update({"_id": result.inserted_id})

    return payload


@app.get("/menu", response_model=list[Item])
async def menu(db: Database):
    items = []
    async for item in db.items.find():
        items.append(item)

    return items


app.mount('/image', StaticFiles(directory="image"), name="image")

app.add_event_handler("startup", database_connect)
app.add_event_handler("shutdown", database_disconnect)
