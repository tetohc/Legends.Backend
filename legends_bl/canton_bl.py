from sqlalchemy.orm import Session
from legends_dal import CantonDAL
from legends_bl.mappers import CantonMapper


class CantonBL:
    """Capa de lógica de negocio para canton"""

    def __init__(self, db: Session):
        self.db = db
        self.canton_dal = CantonDAL(self.db)

    def get_all(self):
        """
        Obtiene todos los cantones desde la capa DAL y los transforma en DTOs.

        **Returns**:
            list: Lista de objetos DTO de cantones.
        """
        cantons = self.canton_dal.get_all()
        return [CantonMapper.convert_to_entity(x) for x in cantons]

    def get_by_id(self, canton_id: int):
        """
        Obtiene un cantón por su identificador único desde la capa DAL y los transforma en DTO.

        **Parámetros**:
            canton_id (int): Identificador único del cantón.

        **Returns**:
            CantonEntity | dict: Objeto DTO del cantón si existe,
                             diccionario con mensaje de error si no.
        """
        result = self.canton_dal.get_by_id(canton_id)
        if "error" in result:
            return result

        return CantonMapper(result)

    def get_by_province(self, province_name: str):
        """
        Obtiene cantones por nombre de provincia desde la capa DAL y lo transforma en DTOs.

        **Parámetros**:
            province_name (str): Nombre de la provincia a buscar.

        **Returns**:
            list | dict: Lista de objetos DTO de cantones si existen, 
                         diccionario con mensaje de error si no.
        """
        result = self.canton_dal.get_by_province(province_name)

        if "error" in result:
            return result

        return [CantonMapper.convert_to_entity(canton) for canton in result]

    def get_by_province_id(self, province_id: int):
        """
        Obtiene cantones por identificador único de provincia desde la capa DAL y los transforma en DTOs.

        **Parámetros**:
            province_id (int): Identificador único de la provincia.

        **Returns**:
            list | dict: Lista de objetos DTO de cantones si existen,
                         diccionario con mensaje de error si no.
        """
        result = self.canton_dal.get_by_province_id(province_id)

        if "error" in result:
            return result

        return [CantonMapper.convert_to_entity(canton) for canton in result]
