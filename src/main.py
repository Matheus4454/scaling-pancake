import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/")
async def read_root():
    return {"message": "Olá Mundo!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# 127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "numero_aleatorio": random.randint(0, 100000)}


@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante



@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0
