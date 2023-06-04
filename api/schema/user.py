from pydantic import Field
from schema.database import ObjectId, DBModel


class User(DBModel):
    name: str = "anonymous"
    mobile: str


class UserIn(User):
    password: str


class UserOut(User):
    id: ObjectId = Field(alias='_id')


class UserDB(User):
    id: ObjectId = Field(alias='_id')
    hashed_password: str
