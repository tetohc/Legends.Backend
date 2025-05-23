from uuid import UUID
from fastapi import APIRouter, Depends, status, Response
from typing import List
from sqlalchemy.orm import Session
from legends_config.database.db_config import get_connection_db
from legends_entities.responses import ApiResponse
from legends_bl import LegendBL
from legends_entities import LegendCreateEntity, LegendEntity

# Creación del objeto router para agrupar los endpoints relacionados con distritos
legends_router = APIRouter(
    prefix="/legends",  # Prefijo URL para todos los endpoints de este router
    tags=["Legends"]  # Categoría en la documentación
)


def get_legend_bl(db: Session = Depends(get_connection_db)):
    """
    Dependencia para inicializar LegendBL con una sesión de la base de datos.

    Parámetros:
        db (Session): Sesión activa de SQLAlchemy obtenida desde `get_connection_db`.

    Returns:
        LegendBL: Instancia de la capa de lógica de negocio con la sesión de base de datos.
    """
    return LegendBL(db)


@legends_router.post(
    "/create",
    response_model=ApiResponse,
    responses={
        status.HTTP_201_CREATED: {"model": ApiResponse},
        status.HTTP_400_BAD_REQUEST: { "model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    }
)
def create(response: Response, create_entity: LegendCreateEntity, legend_bl: LegendBL = Depends(get_legend_bl)):
    """
    Endpoint para crear una nueva leyenda en la base de datos.

    **Parámetros**:
    - `create_entity` (LegendCreateEntity): DTO que representa los datos ingresados por el usuario para registrar una nueva leyenda.

    **Returns**:
    - `ApiResponse`: Estructura de respuesta con el estado, mensaje y datos procesados.

    **Posibles respuestas**:
    - ✅ `201 Created`: La leyenda se ha creado correctamente correctamente. 
    - ❌ `400 Bad Request`: Datos inválidos. La solicitud no cumple con los requisitos esperados.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.
    """
    result = legend_bl.create(create_entity)

    if "error" in result:
        response.status_code = result["status"]
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message=result["error"],
            data=None
        )

    response.status_code = status.HTTP_201_CREATED
    return ApiResponse(
        statusCode=response.status_code,
        success=True,
        message=result["message"],
        data=create_entity
    )


@legends_router.put(
    '/update/{legend_id}',
    response_model=ApiResponse[LegendEntity],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_400_BAD_REQUEST: {"model": ApiResponse},
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    }
)
def update(response: Response, legend_id: UUID, entity: LegendEntity, legend_bl: LegendBL = Depends(get_legend_bl)):
    """
    Endpoint para actualizar una leyenda existente en la base de datos.

    **Parámetros**:
    - `legend_id` (UUID): Identificador único de la leyenda en formato UUID.
    - `entity` (LegendEntity): DTO con los datos actualizados de la leyenda.

    **Returns**:
    - `ApiResponse[LegendEntity]`: Estructura de respuesta con el estado, mensaje y datos procesados.

    **Posibles respuestas**:
    - ✅ `200 OK`: La leyenda se ha actualizado correctamente.
    - ❌ `400 Bad Request`: `legend_id` no fue proporcionado o no tiene un formato válido.
    - ⚠️ `404 Not Found`: La leyenda no existe en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.
    """
    if legend_id is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message="No se proporcionó un ID válido. Por favor, envíe un UUID correcto."
        )

    result = legend_bl.update(entity)
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message="La leyenda no existe en la base de datos"
        )

    if "error" in result:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message=result["error"]
        )

    response.status_code = status.HTTP_200_OK
    return ApiResponse(
        statusCode=response.status_code,
        success=True,
        message=result["message"],
        data=entity
    )


@legends_router.delete(
    "/delete/{legend_id}",
    response_model=ApiResponse,
    responses={
        status.HTTP_204_NO_CONTENT: {"model": None},
        status.HTTP_400_BAD_REQUEST: {"model": ApiResponse},
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    }
)
def delete(response: Response, legend_id: UUID, legend_bl: LegendBL = Depends(get_legend_bl)):
    """
    Endpoint para eliminar una leyenda de la base de datos.

    **Parámetros**:
    - `legend_id` (UUID): Identificador único de la leyenda en formato UUID.

    **Returns**:
    - `ApiResponse`: Estructura de respuesta con el estado y mensaje del resultado.

    **Posibles respuestas**:
    - ✅ `200 OK`: La leyenda se ha eliminado correctamente.
    - ❌ `400 Bad Request`: `legend_id` no fue proporcionado o no tiene un formato válido.
    - ⚠️ `404 Not Found`: La leyenda no existe en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.
    """
    if legend_id is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message="No se proporcionó un ID válido. Por favor, envíe un UUID correcto."
        )

    is_exist = legend_bl.get_by_id(legend_id)
    if is_exist is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message="La leyenda no existe en la base de datos."
        )

    result = legend_bl.delete(legend_id)
    if "error" in result:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message=result["error"]
        )

    response.status_code = status.HTTP_204_NO_CONTENT
    return ApiResponse(
        statusCode=response.status_code,
        success=True,
        message="La leyenda ha sido eliminada correctamente."
    )


@legends_router.get(
    "/{legend_id}",
    response_model=ApiResponse[LegendEntity],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_400_BAD_REQUEST: {"model": ApiResponse},
        status.HTTP_404_NOT_FOUND: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    }
)
def get_by_id(response: Response, legend_id: UUID, legend_bl: LegendBL = Depends(get_legend_bl)):
    """
    Endpoint para obtener una leyenda específica desde la base de datos.

    **Parámetros**:
    - `legend_id` (UUID): Identificador único de la leyenda.

    **Returns**:
    - `ApiResponse[LegendEntity]`: Estructura de respuesta con el estado, mensaje y datos obtenidos.

    **Posibles respuestas**:
    - ✅ `200 OK`: La leyenda ha sido obtenida correctamente.
    - ❌ `400 Bad Request`: `legend_id` no fue proporcionado o no tiene un formato válido.
    - ⚠️ `404 Not Found`: La leyenda no existe en la base de datos.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.
    """
    if legend_id is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message="No se proporcionó un ID válido. Por favor, envíe un UUID correcto."
        )

    result = legend_bl.get_by_id(legend_id)
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message="La leyenda no existe en la base de datos."
        )

    if "error" in result:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message=result["error"]
        )

    response.status_code = status.HTTP_200_OK
    return ApiResponse(
        statusCode=response.status_code,
        success=True,
        message="La leyenda ha sido obtenida correctamente.",
        data=result
    )

@legends_router.get(
    "/",
    response_model=ApiResponse[List[LegendEntity]],
    responses={
        status.HTTP_200_OK: {"model":ApiResponse[List[LegendEntity]]},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse}
    }
)
def get_all(response: Response, legend_bl: LegendBL = Depends(get_legend_bl)):
    """
    Endpoint para obtener todas las leyendas desde la base de datos.

    **Returns**:
    - `ApiResponse[List[LegendEntity]]`: Estructura de respuesta con el estado, mensaje y lista de leyendas.

    **Posibles respuestas**:
    - ✅ `200 OK`: La lista de leyendas ha sido obtenida correctamente.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.
    """
    legends = legend_bl.get_all()

    response.status_code = status.HTTP_200_OK
    return ApiResponse[List[LegendEntity]](
        statusCode=response.status_code,
        success=True,
        message="Lista de leyendas obtenida correctamente.",
        data=legends
    )