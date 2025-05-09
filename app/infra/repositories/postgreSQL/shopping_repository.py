from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.domain.interfaces.entities.ishopping_repository import ShoppingRepositoryInterface
from app.infra.models.shopping_orm import ShoppingORM


class ShoppingRepository(ShoppingRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface):
        self.__db = db

    def create(self, params: dict) -> dict:
        model = ShoppingORM.from_entity(params)
        with self.__db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model.to_entity()
