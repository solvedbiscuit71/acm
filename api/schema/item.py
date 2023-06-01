from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: int
    image_url: str
    is_veg: bool
