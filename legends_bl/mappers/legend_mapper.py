from legends_models import LegendModel
from legends_entities import LegendEntity
from legends_entities import LegendCreateEntity
import uuid


class LegendMapper:
    """"Clase para la conversión entre modelos de base de datos (`LegendModel`) y DTOs """

    @staticmethod
    def convert_to_entity(legend_model: LegendModel) -> LegendEntity:
        """
        Convierte una instancia de `LegendModel` (modelo de base de datos) en `LegendEntity` (DTO).

        **Parámetros**:
        - `legend_model` (LegendModel): Instancia del modelo de base de datos que se convertirá en una entidad.

        **Returns**:
        - `LegendEntity`: Instancia de entidad con los mismos valores que el modelo de base de datos.
        """
        return LegendEntity(
            id=legend_model.id,
            categoryId=legend_model.categoryId,
            districtId=legend_model.districtId,
            name=legend_model.name.strip() if legend_model.name else None,
            description=legend_model.description.strip() if legend_model.description else None,
            imageUrl=legend_model.imageUrl.strip() if legend_model.imageUrl else None,
            date=legend_model.date,
            is_active=legend_model.is_active
        )

    @staticmethod
    def convert_entity_to_model(entity: LegendEntity) -> LegendModel:
        """
        Convierte una instancia de `LegendEntity` (DTO) en `LegendModel` (modelo de base de datos).

        **Parámetros**:
        - `entity` (LegendEntity): Entidad que representa una leyenda existente en el sistema.

        **Returns**:
        - `LegendModel`: Instancia del modelo con los valores listos para ser almacenados en la base de datos.
        """
        return LegendModel(
            id=str(entity.id),
            categoryId=str(entity.categoryId),
            districtId=entity.districtId,
            name=entity.name.strip() if entity.name else None,
            description=entity.description.strip() if entity.description else None,
            imageUrl=entity.imageUrl.strip() if entity.imageUrl else None,
            date=entity.date,
            is_active=entity.is_active
        )

    @staticmethod
    def convert_create_to_model(create_entity: LegendCreateEntity) -> LegendModel:
        """
        Convierte una instancia de `LegendCreateEntity` (DTO) en `LegendModel` (modelo de base de datos).

        **Parámetros**:
        - `create_entity` (LegendCreateEntity): Entidad que representa los datos ingresados por el usuario para crear una leyenda.

        **Returns**:
        - `LegendModel`: Instancia del modelo con los valores listos para ser almacenados en la base de datos.
        """
        return LegendModel(
            id=str(uuid.uuid4()),
            categoryId=create_entity.categoryId,
            districtId=create_entity.districtId,
            name=create_entity.name.strip(),
            description=create_entity.description.strip(),
            imageUrl=create_entity.imageUrl.strip(),
            date=create_entity.date,
            is_active=True
        )
