from pydantic import Field
from schema.database import ObjectId, DBModel


class UserData(DBModel):
    name: str = "anonymous"
    mobile: str = Field(min_length=10, max_length=10, regex="^[0-9]*$")


class UserAuth(DBModel):
    id: ObjectId = Field(alias='_id')
    password: str = Field(min_length=8)


class UserDB(DBModel):
    id: ObjectId = Field(alias='_id')
    hashed_password: str


class UserCreate(UserData):
    password: str = Field(min_length=8)


class UserUpdate(DBModel):
    name: str = None
    mobile: str = Field(default=None, min_length=10,
                        max_length=10, regex="^[0-9]*$")
    password: str = Field(default=None, min_length=8)


class UserId(DBModel):
    id: ObjectId = Field(alias='_id')
