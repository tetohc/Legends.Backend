from sqlalchemy.orm import Session
from legends_bl.mappers import CategoryMapper
from legends_dal import CategoryDAL


class CategoryBL:
    """Capa de lógica de negocio para categorías"""

    def __init__(self, db: Session):
        self.db = db
        self.category_dal = CategoryDAL(self.db)


    def get_all(self):
        """
        Obtiene todas las categoría desde la capa DAL y los transforma en DTOs.

        Returns:
            list: Lista de objetos DTO de categorías.
        """
        categories = self.category_dal.get_all()
        return [CategoryMapper.convert_to_entity(x) for x in categories]
