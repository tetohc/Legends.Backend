from pydantic import BaseModel


class ProvinceEntity(BaseModel):
    """
    DTO (Data Transfer Object) para representar una provincia.

    Atributos:
        id (int): Identificador único de la provincia.
        name (str): Nombre de la provincia.
    """
    id: int
    name: str
