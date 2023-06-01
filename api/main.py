from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/menu")
def menu():
    return {"menu": [], "count": 0}


app.mount('/image', StaticFiles(directory="image"), name="image")
