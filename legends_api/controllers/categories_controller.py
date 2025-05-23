from fastapi import APIRouter, Depends, status, Response
from typing import List
from sqlalchemy.orm import Session
from legends_config.database.db_config import get_connection_db
from legends_entities.responses import ApiResponse
from legends_bl import CategoryBL
from legends_entities import CategoryEntity

categories_router = APIRouter(
    prefix="/categories",  # Prefijo URL para todos los endpoints de este router
    tags=["Categories"]  # Categoría en la documentación
)


def get_category_bl(db: Session = Depends(get_connection_db)):
    """
    Dependencia para inicializar CategoryBL con una sesión de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy obtenida desde `get_connection_db`.

    Returns:
        CategoryBL: Instancia de la capa de lógica de negocio con la sesión de base de datos.
    """
    return CategoryBL(db)


@categories_router.get(
    "/",
    response_model=ApiResponse[List[CategoryEntity]],
    responses={
        status.HTTP_200_OK: {"model": ApiResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ApiResponse},
    }
)
def get_all(response: Response, category_bl: CategoryBL = Depends(get_category_bl)) -> ApiResponse[List[CategoryEntity]]:
    """
    Obtiene todas las categorías registradas en la base de datos.

    **Posibles respuestas**:
    - ✅ `200 OK`: Lista de categorías obtenida correctamente.
    - ⚠️ `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

    **Returns**:
        ApiResponse[List[CategoryEntity]]: Respuesta estructurada con el estado correspondiente.
    """
    try:
        categories = category_bl.get_all()

        response.status_code = status.HTTP_200_OK
        return ApiResponse[List[CategoryEntity]](
            statusCode=response.status_code,
            success=True,
            message="Lista de categorías obtenida correctamente",
            data=categories
        )

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ApiResponse(
            statusCode=response.status_code,
            success=False,
            message=f"Error inesperado: {str(e)}",
            data=None
        )
