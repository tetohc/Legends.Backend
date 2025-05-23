# Importación de módulos necesarios de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Importación de la configuración de la url conexión de la base de datos
from legends_config.settings import settings

SQLACHEMY_DATABASE_URL = settings.database_url
engine = create_engine(SQLACHEMY_DATABASE_URL)

# Configuración de la sesión con SQLAlchemy
# - autocommit=False: Los cambios no se confirman automáticamente
# - autoflush=False: No se envían automáticamente los cambios a la base de datos antes de ejecutar consultas
# - bind=engine: Se vincula la sesión al motor de la base de datos
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_connection_db():
    """
    Generador de sesiones de base de datos.

    Esta función proporciona una conexión a la base de datos utilizando una sesión local.
    La sesión se cierra automáticamente al finalizar el uso.

    Returns:
        db: instancia de la sesión de SQLAlchemy
    """
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
