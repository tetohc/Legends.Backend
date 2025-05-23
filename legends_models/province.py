from legends_config.database.db_config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ProvinceModel(Base):
    """
    Modelo que representa una provincia en la base de datos.

    Atributos:
        id (int): Identificador único de la provincia.
        name (str): Nombre de la provincia.

    Relaciones:
        cantons (List[CantonModel]): Relación uno-a-muchos con los cantones pertenecientes a la provincia.
    """
    __tablename__ = "province"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # Relación un a muchos con CantonModel
    cantons = relationship("CantonModel", back_populates="province")
