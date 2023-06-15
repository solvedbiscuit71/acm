from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends, Body, Header
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from pymongo.results import InsertOneResult, UpdateResult
from pymongo import DESCENDING

from schema.menu import Category
from schema.token import Token, create_access_token, authenticate_access_token, authenticate_waiter_token
from schema.user import UserId, UserCreate, UserUpdate
from schema.order import CartItem, generate_id, Order
from schema.database import database_connect, database_disconnect, ObjectId, Database
from schema.security import hash_password, authenticate_user_id, authenticate_user_mobile, authenticate_waiter
from schema.cors import origins

FILTERS = ('placed', 'preparing', 'ready', 'served')

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
async def update_user(id: Annotated[ObjectId, Depends(authenticate_access_token)], user_data: UserUpdate, db: Database):
    payload = dict()
    if user_data.name:
        payload.update({"name": user_data.name})

    if user_data.password:
        payload.update({"hashed_password": hash_password(user_data.password)})

    if user_data.mobile:
        count = await db.users.count_documents({"mobile": user_data.mobile,
                                                "_id": {"$ne": ObjectId(id)}})
        if count:
            raise HTTPException(status_code=409, detail="mobile already used")
        payload.update({"mobile": user_data.mobile})

    if payload:
        result: UpdateResult = await db.users.update_one({"_id": ObjectId(id)}, {"$set": payload})
        return {"message": "success", "modified_count": result.modified_count}
    else:
        return {"message": "success", "modified_count": 0}


@app.post("/user/token", response_model=Token)
async def create_token(id: Annotated[ObjectId, Depends(authenticate_user_id)]):
    payload = {"_id": str(id)}
    return {"access_token": create_access_token(payload, 'access')}


@app.get("/user/token")
async def verify_token(id: Annotated[str, Depends(authenticate_access_token)]):
    return {"_id": id}

# -------------------
# Waiter
# -------------------


@app.post("/waiter/token", dependencies=[Depends(authenticate_waiter)], response_model=Token)
async def create_waiter_token():
    payload = {"_id": "waiter"}
    return {"access_token": create_access_token(payload, 'waiter')}


@app.get("/waiter/token")
async def verify_token(id: Annotated[str, Depends(authenticate_waiter_token)]):
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

# -------------------
# Order
# -------------------

@app.post("/order")
async def create_order(id: Annotated[str, Depends(authenticate_access_token)], items: list[CartItem], total: Annotated[int, Body()], db: Database):
    new_order = {
        "_id": await generate_id(),
        "user_id": ObjectId(id),
        "items": [item.dict() for item in items],
        "total": total,
        "status": "placed"
    }

    result: InsertOneResult = await db.orders.insert_one(new_order)
    return {"_id": result.inserted_id}

@app.get("/order", response_model=None)
async def get_orders(id: Annotated[str, Depends(authenticate_access_token)], db: Database):
    orders = []
    async for order in db.orders.find({"user_id": ObjectId(id)}, {"user_id": False}).sort('_id', DESCENDING):
        orders.append(order)

    return orders

@app.get("/order/status", response_model=None)
async def get_orders(id: Annotated[str, Depends(authenticate_access_token)], db: Database):
    orders = []
    async for order in db.orders.find({"user_id": ObjectId(id)}, {"status": True}).sort('_id', DESCENDING):
        orders.append(order)

    return orders


@app.get("/order/filter", dependencies=[Depends(authenticate_waiter_token)], response_model=None)
async def get_orders_by_filter(filter: Annotated[str, Header()], db: Database):
    if filter not in FILTERS:
        HTTPException(status_code=400, detail=f"Invalid filter, filter should be one of ({repr(FILTERS)})")
    else:
        orders = []
        pipeline = [
            {"$match": {"status": filter}},
            {"$lookup": { 
                "from": "users",
                "localField": "user_id",
                "foreignField": "_id",
                "as": "user_info" 
            }},
            {"$set": {"user_name": "$user_info.name"}},
            {"$project": {"user_name": {"$arrayElemAt": ['$user_name', 0]}, "items": 1, "total": 1}},
            {"$sort": {"_id": -1}}
        ]
        
        async for order in db.orders.aggregate(pipeline):
            orders.append(order)

        return orders
    pass

app.mount('/image', StaticFiles(directory="image"), name="image")

app.add_event_handler("startup", database_connect)
app.add_event_handler("shutdown", database_disconnect)
