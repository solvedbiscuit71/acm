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

    password = os.getenv("WAITER_SECRET")
    if password:
        if len(password) < 8:
            print("WAITER_SECRET must be atleast 8 characters")

        await db.waiter.insert_one(
            {"_id": "waiter", "hashed_password": hash_password(os.getenv("WAITER_SECRET"))})
        print("Inserted waiter's secret")
    else:
        print("Set a WAITER_SECRET in schema/.env")


async def create_menu():
    db: AsyncIOMotorDatabase = client["acm"]
    await db.categories.drop()
    await db.items.drop()

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

    result = await db.categories.insert_many(categories)
    print(f"Inserted {len(result.inserted_ids)} categories")

    items = []
    modifiers = [str, int, str, str]
    with open(os.getcwd() + os.sep + "assets" + os.sep + "items.csv", "r") as file:
        headers = file.readline()[:-1].split(',')

        while item := file.readline()[:-1]:
            item = item.split(',')
            for i, mod in enumerate(modifiers):
                item[i] = mod(item[i])
            items.append(dict(zip(headers, item)))

    result = await db.items.insert_many(items)
    print(f"Inserted {len(result.inserted_ids)} items")


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

    client.close()

asyncio.run(main())
