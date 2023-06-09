from pymongo import ReturnDocument
from pydantic import Field
from schema.database import DBModel,ObjectId,get_database
from schema.menu import Item

class CartItem(Item):
    quantity: int

class Order(DBModel):
    id: int = Field(alias="_id")
    user_id: ObjectId
    items: list[CartItem]
    total: int
    status: str

async def generate_id() -> int:
    db = get_database()
    result = await db.orders.find_one_and_update(
        {"_id": "item_id"}, 
        {"$inc": {"sequence_value": 1}},
        return_document=ReturnDocument.AFTER)

    return result["sequence_value"]