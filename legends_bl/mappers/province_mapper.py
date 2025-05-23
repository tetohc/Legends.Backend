from legends_entities import ProvinceEntity
from legends_models import ProvinceModel


class ProvinceMapper:
    """Clase para mapear datos entre ProvinceModel y ProvinceEntity"""

    @staticmethod
    def convert_to_entity(province_model: ProvinceModel) -> ProvinceEntity:
        """
        Convierte un modelo ORM en un DTO.

        Parámetros:
            province_model (ProvinceModel): Instancia del modelo de la base de datos.

        Returns:
            ProvinceEntity: DTO con los datos transformados.
        """
        return ProvinceEntity(
            id=province_model.id,
            name=province_model.name.strip() if province_model.name else None
        )
