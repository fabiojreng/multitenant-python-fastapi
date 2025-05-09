from sqlalchemy.exc import NoResultFound

from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.domain.interfaces.entities.icategory_repository import CategoryRepositoryInterface
from app.infra.models.category_orm import CategoryORM


class CategoryRepository(CategoryRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface) -> None:
        self.__db = db

    def list_all(self) -> list[dict]:
        with self.__db.get_session() as session:
            categories = session.query(CategoryORM).all()
            return [category.to_entity() for category in categories]

    def create(self, params: dict) -> list[dict]:
        model = CategoryORM.from_entity(params)
        with self.__db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model.to_entity()

    def find_by_id(self, category_id: str) -> dict:
        with self.__db.get_session() as session:
            try:
                category = session.query(CategoryORM).filter_by(category_id=category_id).one()
                return category.to_entity()
            except NoResultFound:
                return None
