import os
import dotenv

from datetime import datetime, time
from pydantic import BaseModel,Field
from schema.database import get_database, AsyncIOMotorDatabase

dotenv.load_dotenv()
close_time = time.fromisoformat(os.getenv('CLOSE_TIME'))

class Item(BaseModel):
    id: int = Field(alias="_id")
    name: str
    price: int
    image_url: str
    category: str

class Category(BaseModel):
    id: str = Field(alias="_id")
    starts_from: str
    items: list[Item]

class CategoryOut(Category):
    available: bool

async def get_categories():
    db: AsyncIOMotorDatabase = get_database()

    now: time = datetime.now().time()
    categories = []
    async for category in db.menu.find():
        start_time = time(*category["starts_from_time"])
        category.update({"available": close_time > now >= start_time})
        categories.append(category)

    return categories