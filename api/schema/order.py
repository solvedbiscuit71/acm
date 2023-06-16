from fastapi import HTTPException

from pydantic import Field
from pymongo.results import InsertOneResult, UpdateResult
from pymongo import DESCENDING, ReturnDocument

from schema.database import ObjectId, DBModel, AsyncIOMotorDatabase, get_database
from schema.menu import Item

STATUS = ('placed', 'preparing', 'ready', 'served')

class CartItem(Item):
    quantity: int

class Order(DBModel):
    id: int = Field(alias="_id")
    user_id: ObjectId
    items: list[CartItem]
    total: int
    status: str

async def generate_id() -> int:
    db: AsyncIOMotorDatabase = get_database()
    result = await db.orders.find_one_and_update(
        {"_id": "item_id"}, 
        {"$inc": {"sequence_value": 1}},
        return_document=ReturnDocument.AFTER)

    return result["sequence_value"]

async def create_order(user_id: str, items: list[CartItem], total: int):
    db: AsyncIOMotorDatabase = get_database()
    result = await db.orders.find_one_and_update(
        {"_id": "item_id"}, 
        {"$inc": {"sequence_value": 1}},
        return_document=ReturnDocument.AFTER)

    new_order = {
        "_id": result["sequence_value"],
        "user_id": ObjectId(user_id),
        "items": [item.dict() for item in items],
        "total": total,
        "status": "placed"
    }

    result: InsertOneResult = await db.orders.insert_one(new_order)
    return {"_id": result.inserted_id}

async def get_order(id: str):
    db: AsyncIOMotorDatabase = get_database()

    orders = []
    async for order in db.orders.find({"user_id": ObjectId(id)}, {"user_id": False}).sort('_id', DESCENDING):
        orders.append(order)

    return orders


async def get_order_status(id: str):
    db: AsyncIOMotorDatabase = get_database()

    orders = []
    async for order in db.orders.find({"user_id": ObjectId(id)}, {"status": True}).sort('_id', DESCENDING):
        orders.append(order)

    return orders

async def get_order_by_filter(filter: str):
    db: AsyncIOMotorDatabase = get_database()

    if filter in STATUS:
        orders = []
        pipeline = [
            {"$match": {"status": filter}},
            {"$lookup": { 
                "from": "users",
                "localField": "user_id",
                "foreignField": "_id",
                "as": "user_info" 
            }},
            {"$set": {"user_name": "$user_info.name"}},
            {"$project": {"user_name": {"$arrayElemAt": ['$user_name', 0]}, "items": 1, "total": 1}},
            {"$sort": {"_id": -1}}
        ]
        
        async for order in db.orders.aggregate(pipeline):
            orders.append(order)

        return orders
    else:
        raise HTTPException(status_code=400, detail=f"Filter should be one of {STATUS}")

async def update_order_status(id: int, status: str) -> tuple[int, int]:
    db: AsyncIOMotorDatabase = get_database()

    if status in STATUS:
        result: UpdateResult = await db.orders.update_one({"_id": id}, {"$set": {"status": status}})
        return [result.matched_count, result.modified_count]
    else:
        raise HTTPException(status_code=400, detail=f"Status should be one of {STATUS}")