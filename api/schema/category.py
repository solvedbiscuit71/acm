from pydantic import Field, BaseModel


class Category(BaseModel):
    id: str = Field(alias='_id')
    category: str
    starts_from: str
