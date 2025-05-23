from pydantic import BaseModel


class CategoryEntity(BaseModel):
    """
    DTO (Data Transfer Object) para representar una categoría.

    Atributos:
        id (str): Identificador único de la categoría (UUID en formato string)..
        name (str): Nombre de la categoría.
    """
    id: str
    name: str
