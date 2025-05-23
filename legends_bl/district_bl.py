from sqlalchemy.orm import Session
from legends_dal import DistrictDAL
from legends_bl.mappers import DistrictMapper


class DistrictBL:
    """Capa de lógica de negocio para district"""

    def __init__(self, db: Session):
        self.db = db
        self.district_dal = DistrictDAL(self.db)

    def get_all(self):
        """
        Obtiene todos los distritos desde la capa DAL y los transforma en DTOs.

        Returns:
            list: Lista de objetos DTO de distritos.
        """
        districts = self.district_dal.get_all()
        return [DistrictMapper.convert_to_entity(x) for x in districts]

    def get_by_id(self, district_id: int):
        """
        Obtiene un distrito por su identificador único desde la capa DAL y los transforma en DTO.

        Args:
            district_id (int): Identificador único del distrito.

        Returns:
            DistrictEntity | dict: Objeto DTO del distrito si existe,
                             diccionario con mensaje de error si no.
        """
        result = self.district_dal.get_by_id(district_id)
        if "error" in result:
            return result

        return DistrictMapper(result)

    def get_by_canton(self, canton_name: str):
        """
        Obtiene distritos por nombre de cantón desde la capa DAL y los transforma en DTOs.

        Args:
            canton_name (str): Nombre del cantón a buscar.

        Returns:
            list | dict: Lista de objetos DTO de distritos si existen, 
                         diccionario con mensaje de error si no.
        """
        result = self.district_dal.get_by_canton(canton_name)

        if "error" in result:
            return result

        return [DistrictMapper.convert_to_entity(district) for district in result]

    def get_by_canton_id(self, canton_id: int):
        """
        Obtiene distritos por ID de cantón desde la capa DAL y los transforma en DTOs.

        Args:
            canton_id (int): Identificador único del cantón.

        Returns:
            list | dict: Lista de objetos DTO de distritos si existen,
                         diccionario con mensaje de error si no.
        """
        result = self.district_dal.get_by_canton_id(canton_id)

        if "error" in result:
            return result

        return [DistrictMapper.convert_to_entity(district) for district in result]
