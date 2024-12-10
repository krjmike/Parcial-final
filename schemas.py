from pydantic import BaseModel
from datetime import datetime

# Clase base para los productos
class ProductBase(BaseModel):
    titulo: str
    descripcion: str | None = None
    precio: int

# Clase para crear un nuevo producto (hereda de ProductBase)
class ProductCreate(ProductBase):
    pass

# Clase para la salida de un producto
class ProductOut(ProductBase):
    id: int
    dateCreate: datetime
    dateUpdate: datetime

    class Config:
        orm_mode = True
