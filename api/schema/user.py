from pydantic import Field, BaseModel
from schema.database import ObjectId, DBModel


class UserData(DBModel):
    name: str = "anonymous"
    mobile: str = Field(min_length=10, max_length=10, regex="^[0-9]*$")


class UserAuth(DBModel):
    id: ObjectId = Field(alias='_id')
    password: str = Field(min_length=8)


class UserInOptional(DBModel):
    name: str | None = None
    mobile: str | None = Field(
        default=None, min_length=10, max_length=10, regex="^[0-9]*$")
    password: str | None = Field(default=None, min_length=8)


class UserIn(UserData):
    password: str = Field(min_length=8)


class UserOut(UserData):
    id: ObjectId = Field(alias='_id')


class UserDB(UserData):
    id: ObjectId = Field(alias='_id')
    hashed_password: str
