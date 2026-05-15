from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

productos = [
    {"id": 1, "producto": "Monitor", "Precio": 5000},
    {"id": 2, "producto": "Teclado", "Precio": 5000},
    {"id": 3, "producto": "Mouse", "Precio": 5000},
    {"id": 4, "producto": "Celular", "Precio": 5000}
]

class Prducto(BaseModel):
    producto: str
    precio: float

    @app.get("/")
    def get_start():
        return ("clase: Software III")
    
    @app.get("/productos")
    def get_productos():
        return {"Codigo":200, "datos": productos}
    
    @app.get("/productos/{producto_id}")
    def get_producto(producto_id:int):
        for producto in productos:
            if producto ["id"] == producto_id:
                 return {"codigo": 200, "producto":producto}
        raise HTTPException (status_code=404,detail="producto no encontrado")    