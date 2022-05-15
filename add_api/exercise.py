from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


class Addition(BaseModel):
    num1: float
    num2: float


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


db: List[Addition] = [
    Addition(
        num1=6.7,
        num2=6.8,
    ),
]


db1: List[Item] = [
    Item(
        name="Shammah Anucha",
        description="I am a girl",
        price=56.8,
        tax=4.3,
    )
]

app = FastAPI()


@app.get("/")
async def numbers():
    return {"Hello": "World"}


@app.get("/items")
async def get_items():
    return db1


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    db1.append(item)
    return db1


@app.post("/items/update")
async def update_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


# endpoint for adding two numbers
@app.get("/addition")
async def get_numbers():
    return db


@app.post("/addition/sum")
async def add_numbers(item: Addition):
    item_dict = item.dict()
    if item.num1:
        result = item.num1 + item.num2
        item_dict.update({"sum": result})

    return item_dict
