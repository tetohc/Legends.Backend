from legends_config.database.db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class DistrictModel(Base):
    """
    Modelo que representa un distrito en la base de datos.

    Atributos:
        id (int): Identificador único del distrito.
        name (str): Nombre del distrito.
        cantonId (int): Clave foránea que referencia el cantón al que pertenece el distrito.

    Relaciones:
        canton (CantonModel): Relación muchos a uno con el cantón al que pertenece.
        legends (List[LegendModel]): Relación uno a muchos con las leyendas registradas en el distrito.
    """
    __tablename__ = "district"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cantonId = Column(Integer, ForeignKey("canton.id"), nullable=False)

    # Relación muchos a uno con CantonModel
    canton = relationship("CantonModel", back_populates="districts")

    # Relación uno a muchos con LegendModel
    legends = relationship("LegendModel", back_populates="district")
