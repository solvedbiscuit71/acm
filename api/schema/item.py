from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int = Field(alias='_id')
    name: str
    price: int
    image_url: str
    is_veg: bool
