from pydantic import BaseModel,Field

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