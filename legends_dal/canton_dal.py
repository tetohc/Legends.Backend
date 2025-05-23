from sqlalchemy.orm import Session
from legends_models import CantonModel
from legends_models import ProvinceModel


class CantonDAL:
    """Capa de acceso a datos para canton"""

    def __init__(self, db: Session):
        self.db = db  # Recibe una sesión activa de SQLAlchemy

    def get_all(self):
        """
        Obtiene todos los cantones disponibles en la base de datos.

        Returns:
            list: Lista de instancias de CantonModel representando los cantones.
        """
        cantons = self.db.query(CantonModel).all()
        return cantons

    def get_by_id(self, canton_id: int):
        """
        Busca un cantón específico por su identificador único.

        Parámetros:
            canton_id (int): ID del cantón a buscar.

        Returns:
            CantonModel | None: Instancia de CantonModel si se encuentra, None en caso contrario.
        """
        canton = self.db.query(CantonModel).filter(
            CantonModel.id == canton_id).first()

        if not canton:
            return {"error": "El cantón no existe en la base de datos.", "status": 404}

        return canton

    def get_by_province(self, province_name: str):
        """
        Busca cantones por el nombre de la provincia.

        Parámetros:
            province_name (str): Nombre de la provincia a buscar.

        Returns:
            list | dict: Lista de cantones si la provincia existe, 
                         diccionario con un mensaje de error si no.
        """
        try:
            clean_province_name = province_name.strip()

            # Verificar si la provincia existe antes de buscar cantones
            province = self.db.query(ProvinceModel).filter(
                ProvinceModel.name.ilike(clean_province_name)).first()
            if not province:
                return {"error": "La provincia no existe en la base de datos", "status": 404}

            # Obtener cantones asociados a la provincia
            cantons_list = self.db.query(CantonModel).filter(
                CantonModel.provinceId == province.id).all()

            return cantons_list
        except Exception as e:
            return {"error": f"Error en la consulta: {str(e)}", "status": 500}

    def get_by_province_id(self, province_id: int):
        """
        Busca cantones por el identificador de la provincia.

        Parámetros:
            province_id (int): ID de la provincia a buscar.

        Returns:
            list | dict: Lista de cantones si la provincia existe, 
                         diccionario con un mensaje de error si no.
        """
        try:
            # Verificar si la provincia existe antes de buscar cantones
            province = self.db.query(ProvinceModel).filter(
                ProvinceModel.id == province_id).first()
            if not province:
                return {"error": "La provincia no existe en la base de datos", "status": 404}

            # Obtener cantones asociados a la provincia
            cantons_list = self.db.query(CantonModel).filter(
                CantonModel.provinceId == province.id).all()

            return cantons_list
        except Exception as e:
            return {"error": f"Error en la consulta: {str(e)}", "status": 500}
