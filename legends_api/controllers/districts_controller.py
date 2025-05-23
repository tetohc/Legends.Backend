from fastapi import APIRouter, Depends, status, Response
from typing import List
from sqlalchemy.orm import Session
from legends_config.database.db_config import get_connection_db
from legends_entities.responses import ApiResponse
from legends_bl import DistrictBL
from legends_entities.districts import DistrictEntity

# Creación del objeto router para agrupar los endpoints relacionados con distritos
district_router = APIRouter(
    prefix="/districts",  # Prefijo URL para todos los endpoints de este router
    tags=["Districts"]  # Categoría en la documentación 
)


def get_district_bl(db: Session = Depends(get_connection_db)):
    """
    Dependencia para inicializar DistrictBL con una sesión de la base de datos.

    Parámetros:
        db (Session): Sesión activa de SQLAlchemy obtenida desde `get_connection_db`.

    Returns:
        DistrictBL: Instancia de la capa de lógica de negocio con la sesión de base de datos.
    """
    return DistrictBL(db)


@district_router.get(
    "/",
    response_model=ApiResponse[List[DistrictEntity]],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse},
    }
)
def get_all(response: Response, district_bl: DistrictBL = Depends(get_district_bl)) -> ApiResponse[List[DistrictEntity]]:
    """
    Obtiene todos los distritos registrados en la base de datos.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de distritos obtenida correctamente.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[DistrictEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    try:
        districts = district_bl.get_all()

        response.status_code = status.HTTP_200_OK
        return ApiResponse[List[DistrictEntity]](
            statusCode=response.status_code,
            success=True,
            message="Lista de distritos obtenida correctamente",
            data=districts
        )

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message=f"Error inesperado: {str(e)}",
            data=None
        )


@district_router.get(
    "/by-canton/{canton_name}",
    response_model=ApiResponse[List[DistrictEntity]],
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    })
def get_by_canton(response: Response, canton_name: str, district_bl: DistrictBL = Depends(get_district_bl)):
    """
    Obtiene los distritos por el nombre de un cantón.

    **Parámetros**:
    - `canton_name (str)`: Nombre del cantón a buscar.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de distritos obtenida correctamente.
    - ⚠️ `404 Not Found`: No hay distritos de este cantón registrados en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[DistrictEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    result = district_bl.get_by_canton(canton_name)

    if "error" in result:
        response.status_code = result["status"]
        return ApiResponse[List[DistrictEntity]](
            statusCode=response.status_code,
            success=False,
            message=result["error"],
            data=None
        )

    return ApiResponse[List[DistrictEntity]](
        statusCode=status.HTTP_200_OK,
        success=True,
        message="Lista de distritos obtenida correctamente.",
        data=result
    )


@district_router.get(
    "/by-canton-id/{canton_id}",
    response_model=ApiResponse[List[DistrictEntity]],
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    })
def get_by_canton_id(response: Response, canton_id: int, district_bl: DistrictBL = Depends(get_district_bl)):
    """
    Obtiene los distritos por el identificador único de un cantón.

    **Parámetros**:
    - `canton_id (int)`: ID del cantón a buscar.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de distritos obtenida correctamente.
    - ⚠️ `404 Not Found`: No hay distritos registrados en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[DistrictEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    result = district_bl.get_by_canton_id(canton_id)

    if "error" in result:
        response.status_code = result["status"]
        return ApiResponse[List[DistrictEntity]](
            statusCode=response.status_code,
            success=False,
            message=result["error"],
            data=None
        )

    return ApiResponse[List[DistrictEntity]](
        statusCode=status.HTTP_200_OK,
        success=True,
        message="Lista de distritos obtenida correctamente.",
        data=result
    )
