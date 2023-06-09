from pydantic import Field, BaseModel


class Category(BaseModel):
    id: str = Field(alias='_id')
    starts_from: str
