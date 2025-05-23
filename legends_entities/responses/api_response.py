from typing import Optional, TypeVar, Generic,  List, Union
from pydantic import BaseModel

T = TypeVar("T")  # Tipo genérico para permitir reutilización del modelo


class ApiResponse(BaseModel, Generic[T]):
    """
    Modelo estándar de respuesta para la API.

    Esta clase define la estructura de las respuestas que se envían al cliente.

    Atributos:
        statusCode (int): Código de estado HTTP de la respuesta (ej. 200, 400, 500).
        success (bool): Indica si la operación fue exitosa (`True`) o fallida (`False`).
        message (Optional[str]): Mensaje opcional que describe la respuesta (ej. "Operación exitosa").
        data (Optional[T]): Datos de la respuesta, que pueden variar dependiendo del endpoint.
    """

    statusCode: int
    success: bool
    message: Optional[str] = None
    data: Optional[Union[T, List[T]]] = None
