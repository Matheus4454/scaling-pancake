from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Olá": "Mundo!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# 127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "numero_aleatorio": list(range(0, 15))}
