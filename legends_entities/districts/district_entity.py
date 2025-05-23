from pydantic import BaseModel


class DistrictEntity(BaseModel):
    """
    DTO (Data Transfer Object) para representar un distrito.

    Atributos:
        id (int): Identificador único del distrito.
        canton_id (int): Identificador del cantón al que pertenece el distrito.
        name (str): Nombre del distrito.
    """
    id: int
    canton_id: int
    name: str
