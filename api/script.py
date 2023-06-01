import asyncio
import pandas as pd

from motor.motor_asyncio import AsyncIOMotorClient


async def main():
    client = AsyncIOMotorClient()
    acm = client['acm']
    items = acm['items']

    df = pd.read_csv("./assets/items.csv")
    rows = []
    for id, row in df.iterrows():
        row = row.to_dict()
        row['_id'] = 200 + id
        rows.append(row)

    result = await items.insert_many(rows)
    print(f"Inserted {len(result.inserted_ids)}")

asyncio.run(main())
