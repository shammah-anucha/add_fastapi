from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


class Addition(BaseModel):
    num1: float = 8.5
    num2: float = 7.9


app = FastAPI()


@app.get("/")
async def numbers():
    return {"Hello": "World"}


@app.post("/addition/{result}")
async def add_numbers(item: Addition):
    result = item.num1 + item.num2
    return {"result": result}
