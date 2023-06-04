from pydantic import Field
from schema.database import ObjectId, DBModel


class User(DBModel):
    name: str = "anonymous"
    mobile: str = Field(min_length=10, max_length=10, regex="^[0-9]*$")


class UserInOptional(DBModel):
    name: str | None = None
    mobile: str | None = Field(
        default=None, min_length=10, max_length=10, regex="^[0-9]*$")
    password: str | None = Field(default=None, min_length=8)


class UserIn(User):
    password: str = Field(min_length=8)


class UserOut(User):
    id: ObjectId = Field(alias='_id')


class UserDB(User):
    id: ObjectId = Field(alias='_id')
    hashed_password: str
