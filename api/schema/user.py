from pydantic import Field
from schema.database import ObjectId, DBModel


class User(DBModel):
    name: str = "anonymous"
    mobile: str


class UserInOptional(DBModel):
    name: str | None = None
    mobile: str | None = None
    password: str | None = None


class UserIn(User):
    password: str


class UserOut(User):
    id: ObjectId = Field(alias='_id')


class UserDB(User):
    id: ObjectId = Field(alias='_id')
    hashed_password: str
