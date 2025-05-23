from legends_config.database.db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class CantonModel(Base):
    """
    Modelo que representa un cantón en la base de datos.

    Atributos:
        id (int): Identificador único del cantón.
        provinceId (int): Clave foránea que referencia la provincia a la que pertenece el cantón.
        name (str): Nombre del cantón.

    Relaciones:
        province (ProvinceModel): Relación muchos a uno con la provincia a la que pertenece.
        districts (List[DistrictModel]): Relación uno a muchos con los distritos dentro del cantón.
    """
    __tablename__ = "canton"

    id = Column(Integer, primary_key=True)
    provinceId = Column(Integer, ForeignKey("province.id"), nullable=False)
    name = Column(String(50), nullable=False)

    # Relación muchos a uno con ProvinceModel
    province = relationship("ProvinceModel", back_populates="cantons")

    # Relación uno a muchos con DistrictModel
    districts = relationship("DistrictModel", back_populates="canton")
