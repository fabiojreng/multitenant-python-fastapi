from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.domain.interfaces.entities.ibrand_repository import BrandRepositoryInterface
from app.infra.models.brand_orm import BrandORM


class BrandRepository(BrandRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface):
        self.__db = db

    def create(self, params: dict) -> list[dict]:
        model = BrandORM.from_entity(params)
        with self.__db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model.to_entity()

    def list_all(self) -> list[dict]:
        with self.__db.get_session() as session:
            brand_orm = session.query(BrandORM).all()
            return brand_orm

    def find_by_id(self, brand_id: str) -> dict:
        ...
