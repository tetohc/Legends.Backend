from sqlalchemy.orm import Session
from legends_dal import ProvinceDAL
from legends_bl.mappers import ProvinceMapper


class ProvinceBL:
    """Capa de lógica de negocio para province"""

    def __init__(self, db: Session):
        self.db = db
        self.province_dal = ProvinceDAL(self.db)

    def get_all(self):
        """
        Obtiene todas las provincias desde la capa DAL y los transforma en DTOs.

        Returns:
            list: Lista de objetos DTO de provincias.
        """
        provinces = self.province_dal.get_all()
        return [ProvinceMapper.convert_to_entity(x) for x in provinces]

    def get_by_id(self, province_id: int):
        """
        Obtiene una provincia por su identificador único desde la capa DAL y lo transforma en DTO.

        Args:
            province_id (int): Identificador único de la provincia.

        Returns:
            ProvinceEntity | dict: Objeto DTO de la provincia si existe,
                             diccionario con mensaje de error si no.
        """
        result = self.province_dal.get_by_id(province_id)
        if "error" in result:
            return result

        return ProvinceMapper(result)
