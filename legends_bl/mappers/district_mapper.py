from legends_entities import DistrictEntity
from legends_models import DistrictModel


class DistrictMapper:
    """Clase para mapear datos entre DistrictModel y DistrictEntity"""

    @staticmethod
    def convert_to_entity(district_model: DistrictModel) -> DistrictEntity:
        """
        Convierte un modelo ORM en un DTO.

        Args:
            district_model (DistrictModel): Instancia del modelo de la base de datos.

        Returns:
            DistrictEntity: DTO con los datos transformados.
        """
        return DistrictEntity(
            id=district_model.id,
            canton_id=district_model.cantonId,
            name=district_model.name.strip() if district_model.name else None
        )
