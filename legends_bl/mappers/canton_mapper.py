from legends_entities import CantonEntity
from legends_models import CantonModel

class CantonMapper:
    """Clase para mapear datos entre CantonModel y CantonEntity"""

    @staticmethod
    def convert_to_entity(canton_model: CantonModel) -> CantonEntity:
        """
        Convierte un modelo ORM en un DTO.

        Args:
            canton_model (CantonModel): Instancia del modelo de la base de datos.

        Returns:
            CantonEntity: DTO con los datos transformados.
        """
        return CantonEntity(
            id=canton_model.id,
            province_id=canton_model.provinceId,
            name=canton_model.name.strip() if canton_model.name else None
        )