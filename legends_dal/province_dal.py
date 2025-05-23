from sqlalchemy.orm import Session
from legends_models import ProvinceModel

class ProvinceDAL:
    """Capa de acceso a datos de province"""

    def __init__(self, db: Session):
        self.db = db  # Recibe una sesión activa de SQLAlchemy

    def get_all(self):
        """
        Obtiene todas las provincias disponibles en la base de datos.

        Returns:
            list: Lista de instancias de ProvinceModel representando los cantones.
        """
        provinces = self.db.query(ProvinceModel).all()
        return provinces
    
    def get_by_id(self, province_id: int):
        """
        Busca una provincia específica por su identificador único.

        Args:
            province_id (int): Identificador único de la provincia a buscar.

        Returns:
            ProvinceModel | None: Instancia de ProvinceModel si se encuentra, None en caso contrario.
        """
        province = self.db.query(ProvinceModel).filter(
            ProvinceModel.id == province_id).first()

        if not province:
            return {"error": "La provincia no existe en la base de datos.", "status": 404}

        return province