from legends_config.database.db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship


class LegendModel(Base):
    """
    Modelo que representa una leyenda en la base de datos.

    Atributos:
        id (str): Identificador único de la leyenda (UUID en formato string).
        districtId (int): Clave foránea que referencia el distrito donde se origina la leyenda.
        categoryId (str): Clave foránea que referencia la categoría a la que pertenece la leyenda (UUID en formato string).
        name (str): Nombre de la leyenda.
        description (str): Descripción detallada de la leyenda.
        imageUrl (str): URL de la imagen representativa de la leyenda.
        date (date): Fecha en la que se registró o se originó la leyenda.
        is_active (bool): Estado de la leyenda (activo/inactivo).

    Relaciones:
        district (DistrictModel): Relación con el distrito de origen.
        category (CategoryModel): Relación con la categoría a la que pertenece.
    """
    __tablename__ = "legend"

    id = Column(String(36), primary_key=True)
    categoryId = Column(String(36), ForeignKey("category.id"), nullable=False)
    districtId = Column(Integer, ForeignKey("district.id"), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String, nullable=False)
    imageUrl = Column(String(256), nullable=False)
    date = Column(Date, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    # Relación muchos a uno con CategoryModel
    category = relationship("CategoryModel", back_populates="legends")

    # Relación muchos a uno con DistrictModel
    district = relationship("DistrictModel", back_populates="legends")
