from uuid import UUID
from pydantic import BaseModel
from datetime import date as DateType


class LegendEntity(BaseModel):
    """
    DTO (Data Transfer Object) que representa una leyenda.

    Atributos:
        id (str): Identificador único de la leyenda (UUID en formato string).
        categoryId (str): Clave foránea que referencia la categoría de la leyenda (UUID en formato string).
        districtId (int): Clave foránea que referencia el distrito al que pertenece la leyenda.
        name (str): Nombre de la leyenda.
        description (str): Descripción detallada de la leyenda.
        imageUrl (str): URL de la imagen representativa de la leyenda.
        date (date): Fecha en la que se registró o se originó la leyenda.
        is_active (bool): Estado de la leyenda (activo/inactivo).
    """
    id: UUID
    categoryId: str
    districtId: int
    name: str
    description: str
    imageUrl: str
    date: DateType
    is_active: bool
