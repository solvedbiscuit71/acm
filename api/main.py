from fastapi import FastAPI

app = FastAPI()


@app.get("/menu")
def menu():
    return {"menu": [], "count": 0}
