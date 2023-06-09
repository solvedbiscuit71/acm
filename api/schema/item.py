from pydantic import Field
from schema.database import ObjectId, DBModel


class Item(DBModel):
    id: ObjectId = Field(alias='_id')
    name: str
    price: int
    image_url: str
    category: str
