from fastapi import APIRouter, Depends, status, Response
from typing import List
from sqlalchemy.orm import Session
from legends_config.database.db_config import get_connection_db
from legends_entities.responses import ApiResponse
from legends_bl import ProvinceBL
from legends_entities import ProvinceEntity

# Creación del objeto router para agrupar los endpoints relacionados con distritos
provinces_router = APIRouter(
    prefix="/provinces",  # Prefijo URL para todos los endpoints de este router
    tags=["Provinces"]  # Categoría en la documentación
)


def get_province_bl(db: Session = Depends(get_connection_db)):
    """
    Dependencia para inicializar ProvinceBL con una sesión de la base de datos.

    Parámetros:
        db (Session): Sesión activa de SQLAlchemy obtenida desde `get_connection_db`.

    Returns:
        ProvinceBL: Instancia de la capa de lógica de negocio con la sesión de base de datos.
    """
    return ProvinceBL(db)


@provinces_router.get(
    "/",
    response_model=ApiResponse[List[ProvinceEntity]],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse},
    }
)
def get_all(response: Response, province_bl: ProvinceBL = Depends(get_province_bl)) -> ApiResponse[List[ProvinceEntity]]:
    """
    Obtiene todas las provincia registrados en la base de datos.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de provincias obtenida correctamente.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[ProvinceEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    try:
        cantons = province_bl.get_all()

        response.status_code = status.HTTP_200_OK
        return ApiResponse[List[ProvinceEntity]](
            statusCode=response.status_code,
            success=True,
            message="Lista de provincias obtenida correctamente",
            data=cantons
        )

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ApiResponse(
            statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR,
            success=False,
            message=f"Error inesperado: {str(e)}",
            data=None
        )


@provinces_router.get(
    "/{province_id}",
    response_model=ApiResponse[ProvinceEntity],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_400_BAD_REQUEST: {"model": ApiResponse},
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    })
def get_by_id(response: Response, province_id: int, province_bl: ProvinceBL = Depends(get_province_bl)):
    """
    Obtiene los provincias por el identificador único de una provincia.

    **Parámetros**:
    - `province_id (int)`: Identificador único de la provincia a buscar.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de provincias obtenida correctamente.
    - ❌ `400 Bad Request`: Identificador único de provincia inválido.
    - ⚠️ `404 Not Found`: No hay provincias registradas en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[ProvinceEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    if province_id is None or province_id <= 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message="El dentificador único de la provincia no puede ser nulo y debe ser un número positivo",
            data=None
        )

    result = province_bl.get_by_id(province_id)

    if "error" in result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ApiResponse(
            statusCode=status.HTTP_404_NOT_FOUND,
            success=False,
            message=result["error"],
            data=None
        )

    response.status_code = status.HTTP_200_OK
    return ApiResponse[ProvinceEntity](
        statusCode=response.status_code,
        success=True,
        message="Lista de provincias obtenida correctamente.",
        data=result
    )
