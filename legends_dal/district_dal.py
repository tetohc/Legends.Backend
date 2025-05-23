from sqlalchemy.orm import Session
from legends_models import DistrictModel
from legends_models import CantonModel


class DistrictDAL:
    """Capa de acceso a datos para district"""

    def __init__(self, db: Session):
        self.db = db  # Recibe una sesión activa de SQLAlchemy

    def get_all(self):
        """
        Obtiene todos los distritos disponibles en la base de datos.

        Returns:
            list: Lista de instancias de DistrictModel representando los distritos.
        """
        districts = self.db.query(DistrictModel).all()
        return districts

    def get_by_id(self, district_id: int):
        """
        Busca un distrito específico por su identificador único.

        Parámetros:
            district_id (int): ID del distrito a buscar.

        Returns:
            DistrictModel | None: Instancia de DistrictModel si se encuentra, None en caso contrario.
        """
        district = self.db.query(DistrictModel).filter(
            DistrictModel.id == district_id).first()
        return district if district else None

    def get_by_canton(self, canton_name: str):
        """
        Busca distritos por el nombre del cantón.

        Parámetros:
            canton_name (str): Nombre del cantón a buscar.

        Returns:
            list | dict: Lista de distritos si el cantón existe, 
                         diccionario con un mensaje de error si no.
        """
        try:
            clean_canton_name = canton_name.strip()

            # Verificar si el cantón existe antes de buscar distritos
            canton = self.db.query(CantonModel).filter(
                CantonModel.name.ilike(clean_canton_name)).first()
            if not canton:
                return {"error": "El cantón no existe en la base de datos", "status": 404}

            # Obtener distritos asociados al cantón
            districts_list = self.db.query(DistrictModel).filter(
                DistrictModel.cantonId == canton.id).all()

            return districts_list
        except Exception as e:
            return {"error": f"Error en la consulta: {str(e)}", "status": 500}

    def get_by_canton_id(self, canton_id: int):
        """
        Busca distritos por el identificador del cantón.

        Parámetros:
            canton_id (int): ID del cantón a buscar.

        Returns:
            list | dict: Lista de distritos si el cantón existe, 
                         diccionario con un mensaje de error si no.
        """
        try:
            # Verificar si el cantón existe antes de buscar distritos
            canton = self.db.query(CantonModel).filter(
                CantonModel.id == canton_id).first()
            if not canton:
                return {"error": "El cantón no existe en la base de datos", "status": 404}

            # Obtener distritos asociados al cantón
            districts_list = self.db.query(DistrictModel).filter(
                DistrictModel.cantonId == canton.id).all()

            return districts_list
        except Exception as e:
            return {"error": f"Error en la consulta: {str(e)}", "status": 500}
