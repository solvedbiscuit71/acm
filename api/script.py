import sys
import os
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from bcrypt import gensalt

async def create_items():
    client: AsyncIOMotorClient = AsyncIOMotorClient()
    db: AsyncIOMotorDatabase = client["acm"]

    await db.items.drop()

    items = []
    modifiers = [str, int, str, lambda x: bool(x[:-1])]
    with open(os.getcwd() + os.sep + "assets" + os.sep + "items.csv", "r") as file:
        headers = file.readline()[:-1].split(',')

        while item := file.readline():
            item = item.split(',')
            for i, mod in enumerate(modifiers):
                item[i] = mod(item[i])
            items.append(dict(zip(headers, item)))

    result = await db.items.insert_many(items)
    print(f"Inserted {len(result.inserted_ids)} items")

    client.close()


def create_salt():
    with open("schema/.env", "w") as file:
        file.write(f"SALT={gensalt().decode()}")

    print("Generated salt in schema/.env")

async def main():
    arg = sys.argv[1:]

    if '--salt' in arg or '--all' in arg:
        create_salt()
    if '--item' in arg or '--all' in arg:
        await create_items()


asyncio.run(main())
