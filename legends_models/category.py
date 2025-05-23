from legends_config.database.db_config import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class CategoryModel(Base):
    """
    Modelo que representa una categoría de leyendas en la base de datos.

    Atributos:
        id (str): Identificador único de la categoría (UUID en formato string).
        name (str): Nombre de la categoría.

    Relaciones:
        legends (List[LegendModel]): Relación uno a muchos con las leyendas que pertenecen a la categoría.
    """
    __tablename__ = "category"

    id = Column(String(36), primary_key=True)
    name = Column(String(50), nullable=False)

    # Relación uno a muchos con LegendModel
    legends = relationship("LegendModel", back_populates="category")
