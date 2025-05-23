from legends_entities import CategoryEntity
from legends_models import CategoryModel

class CategoryMapper:
    """Clase para mapear datos entre CategoryModel y CategoryEntity"""

    @staticmethod
    def convert_to_entity(category_model: CategoryModel) -> CategoryEntity:
        """
        Convierte un modelo ORM en un DTO.

        Args:
            category_model (CategoryModel): Instancia del modelo de la base de datos.

        Returns:
            CategoryEntity: DTO con los datos transformados.
        """
        return CategoryEntity(
            id=category_model.id,
            name=category_model.name.strip() if category_model.name else None
        )