from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a la base de datos MySQL
DATABASE_URL = "mysql+mysqlconnector://root:c4rt4g3n4@localhost/examen"

# Crear el motor de conexión para la base de datos
engine = create_engine(DATABASE_URL)

# Crear la clase SessionLocal que se usará para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de datos de SQLAlchemy, desde la cual se heredarán todos los modelos
Base = declarative_base()
