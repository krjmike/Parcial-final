from sqlalchemy.orm import Session
import models, schemas

# Función para obtener todos los productos
def get_products(db: Session):
    return db.query(models.Product).all()

# Función para obtener un producto por su ID
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Función para crear un nuevo producto
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())  # Crea un objeto de modelo usando los datos de ProductCreate
    db.add(db_product)  # Añade el nuevo producto a la sesión
    db.commit()  # Confirma la transacción
    db.refresh(db_product)  # Refresca el objeto para obtener los datos actualizados (como el ID)
    return db_product

# Función para actualizar un producto existente
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        for key, value in product.dict().items(): # Actualiza los campos con los nuevos datos 
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product) # Elimina el producto
        db.commit()
    return db_product
