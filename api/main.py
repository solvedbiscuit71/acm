from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from motor.motor_asyncio import AsyncIOMotorClient
from schema.item import Item

client = AsyncIOMotorClient()
acm = client['acm']

app = FastAPI()


@app.get("/menu")
async def menu() -> list[Item]:

    items = []
    async for item in acm.items.find():
        items.append(item)

    return items


app.mount('/image', StaticFiles(directory="image"), name="image")
