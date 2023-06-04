import os
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


async def main():
    client: AsyncIOMotorClient = AsyncIOMotorClient()
    db: AsyncIOMotorDatabase = client["acm"]

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

asyncio.run(main())
