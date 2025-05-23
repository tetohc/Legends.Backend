from pydantic import BaseModel


class CantonEntity(BaseModel):
    """
    DTO (Data Transfer Object) para representar un cantón.

    Atributos:
        id (int): Identificador único del cantón.
        province_id (int): Identificador de la provincia a la que pertenece el cantón.
        name (str): Nombre del cantón.
    """
    id: int
    province_id: int
    name: str
