from uuid import UUID
from sqlalchemy.orm import Session
from legends_dal import LegendDAL
from legends_bl.mappers import LegendMapper
from legends_entities import LegendEntity, LegendCreateEntity


class LegendBL:
    """Capa de lógica de negocio para legend"""

    def __init__(self, db: Session):
        self.db = db
        self.legend_dal = LegendDAL(self.db)

    def create(self, create_entity: LegendCreateEntity):
        """
        Crea una nueva leyenda en la base de datos a través de la capa DAL.

        **Parámetros**:
        - `create_entity` (LegendCreateEntity): DTO que representa los datos ingresados por el usuario para registrar una nueva leyenda.

        **Returns**:
        - Diccionario con mensaje de éxito y código de estado `201` si la operación es exitosa.
        - Diccionario con mensaje de error y código de estado `500` si ocurre un fallo en la capa BL.
        """
        try:
            model = LegendMapper.convert_create_to_model(create_entity)
            return self.legend_dal.create(model)
        except Exception as e:
            return {"error": f"Error en la capa BL al crear la leyenda: {str(e)}", "status": 500}

    def update(self, entity: LegendEntity):
        """
        Actualiza una leyenda existente en la base de datos a través de la capa DAL.

        **Parámetros**:
        - `entity` (LegendEntity): DTO que representa los datos actualizados de la leyenda.

        **Returns**:
        - Diccionario con `"status"` y mensaje de éxito si la operación es exitosa.
        - Diccionario con `"error"` y código de estado `404` si la leyenda no existe.
        - Diccionario con `"error"` y código de estado `500` si ocurre un fallo inesperado en la capa BL.
        """
        try:
            legend = self.legend_dal.get_by_id(str(entity.id))
            if isinstance(legend, dict) or legend is None:
                return legend

            legend.categoryId = str(entity.categoryId)
            legend.districtId = entity.districtId
            legend.name = entity.name.strip() if entity.name else None
            legend.description = entity.description.strip() if entity.description else None
            legend.imageUrl = entity.imageUrl.strip() if entity.imageUrl else None
            legend.date = entity.date
            legend.is_active = entity.is_active
            
            result = self.legend_dal.update(legend)
            return result
        except Exception as e:
            return {"error": f"Error en la capa BL al actualizar la leyenda: {str(e)}", "status": 500}

    def delete(self, legend_id: UUID):
        """
        Desactiva una leyenda existente en la base de datos, realizando un borrado lógico.

        **Parámetros**:
        - `legend_id` (UUID): Identificador único de la leyenda a eliminar.

        **Returns**:
        - Diccionario con `"status"` y mensaje de éxito si la operación es exitosa.
        - Diccionario con `"error"` y código de estado `404` si la leyenda no existe.
        - Diccionario con `"error"` y código de estado `500` si ocurre un fallo inesperado.
        """
        legend = self.legend_dal.get_by_id(str(legend_id))
        if legend is None:
            return legend

        legend.is_active = False
        result = self.legend_dal.update(legend)
        return result

    def get_by_id(self, legend_id: UUID):
        """
        Obtiene una leyenda específica desde la capa DAL y la transforma en un DTO.

        **Parámetros**:
        - `legend_id` (str): Identificador único de la leyenda a buscar.

        **Returns**:
        - Objeto DTO de la leyenda si existe en la base de datos.
        - Diccionario con mensaje de error y código de estado si ocurre un problema.
        """
        legend = self.legend_dal.get_by_id(str(legend_id))
        if legend is None:
            return legend

        if isinstance(legend, dict) and "error" in legend:
            return legend

        return LegendMapper.convert_to_entity(legend)

    def get_all(self, skip: int = 0, limit: int = 10):
        """
        Obtiene todas las leyendas desde la capa DAL con soporte para paginación y las transforma en DTOs.

        **Parámetros**:
        - `skip` (int): Cantidad de registros a omitir (para paginación).
        - `limit` (int): Cantidad máxima de registros a devolver.

        **Returns**:
        - Lista de objetos DTO de leyendas si la consulta es exitosa.
        - Diccionario con `"error"` y `"status"` en caso de fallo.
        """
        legends = self.legend_dal.get_all(skip, limit)
        if isinstance(legends, dict) and "error" in legends:
            return legends

        return [LegendMapper.convert_to_entity(x) for x in legends]
