from sqlalchemy.exc import NoResultFound

from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.domain.interfaces.entities.isupplier_repository import SupplierRepositoryInterface
from app.infra.models.supplier_orm import SupplierORM


class SupplierRepository(SupplierRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface):
        self.__db = db

    def create(self, params: dict) -> dict:
        model = SupplierORM.from_entity(params)
        with self.__db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model.to_entity()

    def list_all(self) -> list[dict]:
        with self.__db.get_session() as session:
            suppliers_orm = session.query(SupplierORM).all()
            return [supplier.to_entity() for supplier in suppliers_orm]

    def find_by_id(self, supplier_id: str) -> dict | None:
        with self.__db.get_session() as session:
            try:
                supplier = session.query(SupplierORM).filter_by(supplier_id=supplier_id).one()
                return supplier.to_entity()
            except NoResultFound:
                return None

    def find_by_email(self, email: str) -> dict | None:
        with self.__db.get_session() as session:
            try:
                supplier = session.query(SupplierORM).filter_by(email=email).first()
                return supplier.to_entity()
            except NoResultFound:
                return None
