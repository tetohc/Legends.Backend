from fastapi import APIRouter, Depends, status, Response
from typing import List
from sqlalchemy.orm import Session
from legends_config.database.db_config import get_connection_db
from legends_entities.responses import ApiResponse
from legends_bl import CantonBL
from legends_entities import CantonEntity

# Creación del objeto router para agrupar los endpoints relacionados con distritos
cantons_router = APIRouter(
    prefix="/cantons",  # Prefijo URL para todos los endpoints de este router
    tags=["Cantons"]  # Categoría en la documentación
)


def get_canton_bl(db: Session = Depends(get_connection_db)):
    """
    Dependencia para inicializar CantonBL con una sesión de la base de datos.

    Parámetros:
        db (Session): Sesión activa de SQLAlchemy obtenida desde `get_connection_db`.

    Returns:
        CantonBL: Instancia de la capa de lógica de negocio con la sesión de base de datos.
    """
    return CantonBL(db)


@cantons_router.get(
    "/",
    response_model=ApiResponse[List[CantonEntity]],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse},
    }
)
def get_all(response: Response, canton_bl: CantonBL = Depends(get_canton_bl)) -> ApiResponse[List[CantonEntity]]:
    """
    Obtiene todos los cantones registrados en la base de datos.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de cantones obtenida correctamente.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[CantonEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    try:
        cantons = canton_bl.get_all()

        response.status_code = status.HTTP_200_OK
        return ApiResponse[List[CantonEntity]](
            statusCode=response.status_code,
            success=True,
            message="Lista de cantones obtenida correctamente",
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


@cantons_router.get(
    "/by-province/{province_name}",
    response_model=ApiResponse[List[CantonEntity]],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    })
def get_by_province(response: Response, province_name: str, canton_bl: CantonBL = Depends(get_canton_bl)):
    """
    Obtiene los cantones por el nombre de una provincia.

    **Parámetros**:
    - `provincia_name (str)`: Nombre de la provincia a buscar.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de los cantones obtenida correctamente.
    - ⚠️ `404 Not Found`: No hay distritos registrados en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[CantonEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    result = canton_bl.get_by_province(province_name)

    if "error" in result:
        response.status_code = result["status"]
        return ApiResponse[List[CantonEntity]](
            statusCode=response.status_code,
            success=False,
            message=result["error"],
            data=None
        )

    return ApiResponse[List[CantonEntity]](
        statusCode=status.HTTP_200_OK,
        success=True,
        message="Lista de cantones obtenida correctamente.",
        data=result
    )

@cantons_router.get(
    "/by-province-id/{province_id}",
    response_model=ApiResponse[List[CantonEntity]],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    })
def get_by_province_id(response: Response, province_id: int, canton_bl: CantonBL = Depends(get_canton_bl)):
    """
    Endpoint para obtener los cantones por el identificador único de una provincia.

    **Parámetros**:
    - `province_id (int)`: Identificador único de la provincia a buscar.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de cantones obtenida correctamente.
    - ⚠️ `404 Not Found`: No hay cantones registrados en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[CantonEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    result = canton_bl.get_by_province_id(province_id)

    if "error" in result:
        response.status_code = result["status"]
        return ApiResponse[List[CantonEntity]](
            statusCode=response.status_code,
            success=False,
            message=result["error"],
            data=None
        )

    return ApiResponse[List[CantonEntity]](
        statusCode=status.HTTP_200_OK,
        success=True,
        message="Lista de cantones obtenida correctamente.",
        data=result
    )
