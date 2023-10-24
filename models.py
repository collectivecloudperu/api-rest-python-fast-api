from sqlalchemy.types import Integer, VARCHAR, TIMESTAMP

from pydantic import BaseModel

class Bicicletas(BaseModel):
    id: int
    nombre: str | None = None
    precio: str | None = None
    stock: str | None = None
