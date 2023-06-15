from pydantic import Field, BaseModel


class Waiter(BaseModel):
    id: str = "waiter"
    password: str = Field(min_length=8)
