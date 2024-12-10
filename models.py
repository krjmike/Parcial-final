from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from datetime import datetime, timezone, timedelta
from database import Base

# Define la zona horaria de Colombia (UTC -5)
colombia_tz = timezone(timedelta(hours=-5))

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(50), index=True)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Integer, nullable=False)
    dateCreate = Column(DateTime, default=datetime.now(colombia_tz))  # Fecha automática al crear
    dateUpdate = Column(DateTime, default=lambda:datetime.now(colombia_tz), onupdate=lambda:datetime.now(colombia_tz))  # Fecha automática al actualizar
