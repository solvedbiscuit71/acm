import sys
import os
import dotenv
import asyncio

from schema.security import hash_password
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from bcrypt import gensalt

dotenv.load_dotenv("./schema/.env")

client: AsyncIOMotorClient = AsyncIOMotorClient()


async def create_waiter():
    db: AsyncIOMotorDatabase = client["acm"]
    await db.waiter.drop()

    password = os.getenv("WAITER_PASSWORD")
    if password:
        if len(password) < 8:
            print("WAITER_PASSWORD must be atleast 8 characters")
            return

        await db.waiter.insert_one(
            {"_id": "waiter", "hashed_password": hash_password(os.getenv("WAITER_SECRET"))})
        print("Inserted waiter's secret")
    else:
        print("Set a WAITER_PASSWORD in schema/.env")


async def create_menu():
    db: AsyncIOMotorDatabase = client["acm"]
    await db.menu.drop()

    categories = []
    modifiers = [str, str]
    with open(os.getcwd() + os.sep + "assets" + os.sep + "categories.csv", "r") as file:
        headers = file.readline()[:-1].split(',')
        headers[0] = "_id"

        while category := file.readline()[:-1]:
            category = category.split(',')
            for i, mod in enumerate(modifiers):
                category[i] = mod(category[i])
            categories.append(dict(zip(headers, category)))


    
    items, id = [], 200
    modifiers = [str, int, str, str]
    with open(os.getcwd() + os.sep + "assets" + os.sep + "items.csv", "r") as file:
        headers = file.readline()[:-1].split(',')

        while item := file.readline()[:-1]:
            item = item.split(',')
            for i, mod in enumerate(modifiers):
                item[i] = mod(item[i])

            item = dict(zip(headers, item))
            item.update({"_id": id})
            id += 1

            items.append(item)

    for category in categories:
        name = category["_id"]
        category_items = [item for item in items if item["category"] == name]
        category.update({"items": category_items})
    
    result = await db.menu.insert_many(categories)
    print(f"Inserted {result.inserted_ids} categories")

async def create_order():
    db: AsyncIOMotorDatabase = client["acm"]
    await db.orders.drop()

    try:
        gen = {"_id": "item_id", "sequence_value": int(os.getenv("SEQ_START"))}
        await db.orders.insert_one(gen)

        print("Created sequence generator for orders")
    except ValueError:
        print("SEQ_START must be integer")


def create_salt():
    with open("schema/.env", "w") as file:
        file.write(f"SALT={gensalt().decode()}")

    print("Generated salt in schema/.env")


async def main():
    arg = sys.argv[1:]

    if '--salt' in arg or '--all' in arg:
        create_salt()
    if '--menu' in arg or '--all' in arg:
        await create_menu()
    if '--waiter' in arg or '--all' in arg:
        await create_waiter()
    if '--order' in arg or '--all' in arg:
        await create_order()

    client.close()

asyncio.run(main())
