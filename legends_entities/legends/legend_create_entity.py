from pydantic import BaseModel, Field
from datetime import date as DateType


class LegendCreateEntity(BaseModel):
    """
    **DTO para la creación de una leyenda.**

    **Atributos**:
    - `categoryId` (str): Identificador de la categoría a la que pertenece la leyenda.
    - `districtId` (int): Identificador del distrito asociado a la leyenda.
    - `name` (str): Nombre de la leyenda. Debe ser único y descriptivo.
    - `description` (str): Descripción detallada de la leyenda.
    - `imageUrl` (str): URL de la imagen representativa de la leyenda.
    - `date` (date): Fecha relacionada con la leyenda (puede ser su origen o una fecha relevante).
    """
    categoryId: str = Field(..., title="ID de Categoría",
                            description="Identificador único de la categoría de la leyenda")
    districtId: int = Field(..., title="ID de Distrito",
                            description="Identificador único del distrito asociado")
    name: str = Field(..., title="Nombre de Leyenda",
                      description="Nombre de la leyenda", max_length=50)
    description: str = Field(..., title="Descripción",
                             description="Detalles de la leyenda")
    imageUrl: str = Field(..., title="URL de Imagen",
                          description="Enlace a la imagen representativa de la leyenda")
    date: DateType = Field(..., title="Fecha de la Leyenda",
                           description="Fecha asociada a la leyenda")
