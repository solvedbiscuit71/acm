from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: int
    image_url: str
    is_veg: bool
