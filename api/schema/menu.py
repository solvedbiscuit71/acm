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
    out_of_stock: bool

class Category(BaseModel):
    id: str = Field(alias="_id")
    starts_from: str
    items: list[Item]

class CategoryOut(Category):
    available: bool

async def get_menu():
    db: AsyncIOMotorDatabase = get_database()

    pipeline = [
        {
            "$lookup": {
                "from": "items",
                "localField": "items_id",
                "foreignField": "_id",
                "as": "items_info"
            }
        },
        {
            "$project": {
                "starts_from": 1,
                "starts_from_time": 1,
                "items": "$items_info"
            }
        }
    ]

    now: time = datetime.now().time()
    categories = []
    async for category in db.categories.aggregate(pipeline):
        start_time = time.fromisoformat(category["starts_from_time"])
        category.update({"available": close_time > now >= start_time})
        categories.append(category)

    return categories

async def get_categories():
    db: AsyncIOMotorDatabase = get_database()

    categories = []
    async for category in db.categories.find({}, {"_id": 0, "name": "$_id"}):
        categories.append(category)

    return categories

async def get_items_by_filter(filter: str):
    db: AsyncIOMotorDatabase = get_database()

    items = []
    async for item in db.items.find({"category_id": filter}):
        items.append(item)

    return items