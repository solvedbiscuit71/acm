from typing import Annotated
from datetime import datetime, time

from fastapi import FastAPI, HTTPException, Depends, Body, Header
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from pymongo.results import InsertOneResult, UpdateResult
from pymongo import DESCENDING

from schema.menu import Category, get_categories
from schema.token import Token, create_access_token, authenticate_access_token, authenticate_waiter_token
from schema.user import UserId, UserCreate, UserUpdate, create_user, update_user, authenticate_user_id, authenticate_user_mobile
from schema.order import CartItem, generate_id
from schema.database import database_connect, database_disconnect, ObjectId, Database
from schema.security import authenticate_waiter
from schema.cors import origins

STATUS = ('placed', 'preparing', 'ready', 'served')

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
async def handle_get_user(id: Annotated[ObjectId, Depends(authenticate_user_mobile)]):
    return {"_id": id}


@app.post("/user", response_model=UserId)
async def handle_post_user(user_data: UserCreate):
    return await create_user(user_data)


@app.patch("/user", response_model=None)
async def handle_patch_user(id: Annotated[ObjectId, Depends(authenticate_access_token)], user_data: UserUpdate):
    result: tuple[int, int] = await update_user(id, user_data)

    match result:
        case (0, _):
            raise HTTPException(status_code=400, detail="Invalid id")
        case (_, 0):
            return {"message": "not modified"}
        case _:
            return {"message": "modified"}


@app.get("/user/token")
async def handle_get_user_token(id: Annotated[str, Depends(authenticate_access_token)]):
    return {"_id": id}


@app.post("/user/token", response_model=Token)
async def handle_post_user_token(id: Annotated[ObjectId, Depends(authenticate_user_id)]):
    return create_access_token({"_id": str(id)}, 'access')

# -------------------
# Waiter
# -------------------

@app.get("/waiter/token")
async def verify_token(id: Annotated[str, Depends(authenticate_waiter_token)]):
    return {"_id": id}


@app.post("/waiter/token", dependencies=[Depends(authenticate_waiter)], response_model=Token)
async def create_waiter_token():
    return create_access_token({"_id": "waiter"}, 'waiter')

# -------------------
# Menu
# -------------------

@app.get("/menu", response_model=list[Category])
async def fetch_categories():
    return await get_categories()

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
    if filter not in STATUS:
        raise HTTPException(status_code=400, detail=f"Filter should be one of {STATUS}")
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

@app.patch("/order/{id}", dependencies=[Depends(authenticate_waiter_token)], response_model=None)
async def get_orders_by_filter(id: int, status: Annotated[str, Header()], db: Database):
    if status not in STATUS:
        raise HTTPException(status_code=400, detail=f"Status should be one of {STATUS}")
    else:
        result: UpdateResult = await db.orders.update_one({"_id": id}, {"$set": {"status": status}})
        if result.modified_count > 0:
            return {"message": "success"}
        elif result.matched_count > 0:
            return {"message": "no modification"}
        else:
            raise HTTPException(status_code=400, detail="Invalid id")

app.mount('/image', StaticFiles(directory="image"), name="image")

app.add_event_handler("startup", database_connect)
app.add_event_handler("shutdown", database_disconnect)
