"""Crud to use mongo db as database."""

import math
import random

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Configuration of the MongoDB connection
MONGODB_URI = (
    "mongodb+srv://jamesacosta:Elmundoesgrande123_"
    "@fasapi.xxvlvla.mongodb.net/?retryWrites=true&w="
    "majority&appName=fasapi"
)
client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))
db = client["fastapi_db"]  # Database nameos
names_collection = db["names"]  # Collection name
app = FastAPI()
templates = Jinja2Templates(directory="templates")


class NameItem(BaseModel):
    """Pydantic model for representing a name in the database."""
    name: str


@app.post("/name", response_class=HTMLResponse)
async def create_name(name_item: NameItem, request: Request):
    """Endpoint to create a new name."""
    # Inserts the name in the database
    names_collection.insert_one(name_item.dict())
    # Retrieves all names from the database
    names_cursor = names_collection.find({}, {"_id": 0, "name": 1})
    # Creates a list of tuples (index, name)
    names = [(index + 1, name["name"]) for index, name in enumerate(names_cursor)]
    return templates.TemplateResponse(
        "names.html",
        {"request": request, "indexed_names": names, "new_name": name_item.name},
    )


@app.get("/", response_class=HTMLResponse)
async def read_names(request: Request):
    """Endpoint to read existing names."""
    names_cursor = names_collection.find({}, {"_id": 0, "name": 1})
    indexed_names = [(index + 1, name["name"]) for index, name in enumerate(names_cursor)]
    return templates.TemplateResponse(
        "names.html", {"request": request, "indexed_names": indexed_names}
    )


@app.put("/name/{name_id}")
async def update_name(name_id: str, name_item: NameItem):
    """Endpoint to update an existing name."""
    result = names_collection.update_one({"_id": name_id}, {"$set": name_item.dict()})
    if result.matched_count:
        return {"message": "Name updated successfully"}
    raise HTTPException(status_code=404, detail="Name not found")


@app.delete("/name/{index}")
def delete_name(index: int):
    """Endpoint to delete an existing name by its index."""
    # Convert index to a position within the collection (0-indexed)
    index -= 1
    if index < 0:
        raise HTTPException(status_code=400, detail="Invalid index")

    # Find the name in the desired position
    name_to_delete = None
    for name in names_collection.find().skip(index).limit(1):
        name_to_delete = name

    # If the name was found, delete it
    if name_to_delete:
        result = names_collection.delete_one({'_id': name_to_delete.get('_id')})
        if result.deleted_count:
            return {"message": "Name deleted successfully"}
    raise HTTPException(status_code=404, detail="Name not found")

@app.get("/sin/{number}", response_class=HTMLResponse)
async def calculate_sin(number: float, request: Request):
    """Endpoint to calculate the sine of a number."""
    sin_res = math.sin(number)
    return templates.TemplateResponse(
        "seno.html", {"request": request, "sin_res": sin_res}
    )


@app.get("/cos/{number}", response_class=HTMLResponse)
async def calculate_cos(number: float, request: Request):
    """Endpoint para calcular el coseno de un número."""
    cos_res = math.cos(number)
    return templates.TemplateResponse(
        "cos.html", {"request": request, "cos_res": cos_res}
    )


@app.get("/random_number", response_class=HTMLResponse)
async def generate_random(request: Request):
    """Endpoint para generar un número aleatorio entre 0 y 10."""
    random_number = random.randint(0, 10)
    return templates.TemplateResponse(
        "random.html", {"request": request, "random_number": random_number}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5050)
