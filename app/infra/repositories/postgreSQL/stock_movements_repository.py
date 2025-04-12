from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.domain.interfaces.entities.istock_movements_repository import StockMovementsRepositoryInterface
from app.infra.models.stock_movements_orm import StockMovementORM


class StockMovementsRepository(StockMovementsRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface):
        self.__db = db

    def list_all(self) -> list[dict]:
        with self.__db.get_session() as session:
            movements_orm = session.query(StockMovementORM).all()
            return [movement.to_entity() for movement in movements_orm]

    def create(self, params: dict) -> dict:
        model = StockMovementORM.from_entity(params)
        with self.__db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model.to_entity()
