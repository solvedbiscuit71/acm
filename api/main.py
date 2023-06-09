from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from pymongo.results import InsertOneResult, UpdateResult

from schema.menu import Category
from schema.token import Token, create_access_token, authenticate_token
from schema.user import UserId, UserCreate, UserUpdate
from schema.database import database_connect, database_disconnect, ObjectId, Database
from schema.security import hash_password, authenticate_user_id, authenticate_user_mobile, authenticate_waiter
from schema.cors import origins


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------
# User Authentication
# -------------------


@app.get("/user", response_model=UserId)
async def get_user(id: Annotated[ObjectId, Depends(authenticate_user_mobile)]):
    return {"_id": id}


@app.post("/user", response_model=UserId)
async def create_user(user_data: UserCreate, db: Database):
    payload = user_data.dict()
    payload.pop("password")
    payload.update({"hashed_password": hash_password(user_data.password)})

    count = await db.users.count_documents({"mobile": user_data.mobile})
    if count:
        raise HTTPException(status_code=409, detail="mobile already used")

    result: InsertOneResult = await db.users.insert_one(payload)
    return {"_id": result.inserted_id}


@app.patch("/user", response_model=None)
async def update_user(id: Annotated[ObjectId, Depends(authenticate_token)], user_data: UserUpdate, db: Database):
    payload = dict()
    if user_data.name:
        payload.update({"name": user_data.name})

    if user_data.password:
        payload.update({"hashed_password": hash_password(user_data.password)})

    if user_data.mobile:
        count = await db.users.count_documents({"mobile": user_data.mobile,
                                                "_id": {"$ne": id}})
        if count:
            raise HTTPException(status_code=409, detail="mobile already used")
        payload.update({"mobile": user_data.mobile})

    if payload:
        result: UpdateResult = await db.users.update_one({"_id": id}, {"$set": payload})
        return {"message": "success", "modified_count": result.modified_count}
    else:
        return {"message": "success", "modified_count": 0}


@app.post("/user/token", response_model=Token)
async def create_token(id: Annotated[ObjectId, Depends(authenticate_user_id)]):
    payload = {"_id": str(id)}
    return {"access_token": create_access_token(payload)}


@app.get("/user/token")
async def verify_token(id: Annotated[str, Depends(authenticate_token)]):
    return {"_id": id}

# -------------------
# Waiter
# -------------------


@app.post("/waiter/token", dependencies=[Depends(authenticate_waiter)], response_model=Token)
async def create_waiter_token():
    payload = {"_id": "waiter"}
    return {"access_token": create_access_token(payload)}


@app.get("/waiter/token")
async def verify_token(id: Annotated[str, Depends(authenticate_token)]):
    return {"_id": id}

# -------------------
# Menu
# -------------------

@app.get("/menu", response_model=list[Category])
async def fetch_categories(db: Database):
    categories = []
    async for category in db.menu.find():
        categories.append(category)

    return categories

app.mount('/image', StaticFiles(directory="image"), name="image")

app.add_event_handler("startup", database_connect)
app.add_event_handler("shutdown", database_disconnect)
