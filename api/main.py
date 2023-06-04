from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from motor.motor_asyncio import AsyncIOMotorDatabase

from schema.item import Item
from schema.database import get_database, database_connect, database_disconnect

app = FastAPI()


@app.get("/menu", response_model=list[Item])
async def menu(db: Annotated[AsyncIOMotorDatabase, Depends(get_database)]):
    items = []
    async for item in db.items.find():
        items.append(item)

    return items


app.mount('/image', StaticFiles(directory="image"), name="image")

app.add_event_handler("startup", database_connect)
app.add_event_handler("shutdown", database_disconnect)
