"""
Este módulo contiene la lógica para una aplicación FastAPI.
"""

import math
import random

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="../templates")


class NameItem(BaseModel):
    """Modelo para un nombre."""

    name: str


names = []


@app.post("/name", response_class=HTMLResponse)
async def create_name(name_item: NameItem, request: Request):
    """Crea un nuevo nombre."""
    names.append(name_item.name)
    response = templates.TemplateResponse(
        "names.html", {"request": request, "names": names, "new_name": name_item.name}
    )
    return response


@app.get("/", response_class=HTMLResponse)
async def read_names(request: Request):
    """Lee los nombres existentes."""
    indexed_names = [(index + 0, name) for index, name in enumerate(names)]
    return templates.TemplateResponse(
        "names.html", {"request": request, "indexed_names": indexed_names}
    )


@app.put("/name/{index}")
async def update_name(index: int, updated_name: str):
    """Actualiza un nombre existente."""
    if 0 <= index < len(names):
        names[index] = updated_name
        return {"message": "Name updated successfully"}
    return {"error": "Index out of range"}


@app.delete("/name/{index}")
async def delete_name(index: int):
    """Elimina un nombre existente."""
    if 0 <= index < len(names):
        deleted_name = names.pop(index)
        return {"message": f"Name '{deleted_name}' deleted successfully"}
    return {"error": "Index out of range"}


@app.get("/sin/{number}", response_class=HTMLResponse)
async def calculate_sin(number: float, request: Request):
    """Calcula el seno de un número."""
    sin_res = math.sin(number)
    return templates.TemplateResponse(
        "seno.html", {"request": request, "sin_res": sin_res}
    )


@app.get("/cos/{number}", response_class=HTMLResponse)
async def calculate_cos(number: float, request: Request):
    """Calcula el coseno de un número."""
    cos_res = math.cos(number)
    return templates.TemplateResponse(
        "cos.html", {"request": request, "cos_res": cos_res}
    )


@app.get("/random_number", response_class=HTMLResponse)
async def generate_random(request: Request):
    """Genera un número aleatorio."""
    min_number = 0
    max_number = 10
    random_number = random.randint(min_number, max_number)
    return templates.TemplateResponse(
        "random.html", {"request": request, "random_number": random_number}
    )
