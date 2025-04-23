from sqlalchemy.exc import NoResultFound

from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.domain.interfaces.entities.iproduct_repository import ProductRepositoryInterface
from app.infra.models.product_orm import ProductORM


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface):
        self.__db = db

    def list_all(self) -> list[dict]:
        with self.__db.get_session() as session:
            products_orm = session.query(ProductORM).all()
            return [product.to_entity() for product in products_orm]

    def create(self, params: dict) -> dict:
        model = ProductORM.from_entity(params)
        with self.__db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model.to_entity()

    def find_by_id(self, product_id: int) -> dict:
        with self.__db.get_session() as session:
            try:
                product = session.query(ProductORM).filter_by(product_id=product_id).one()
                return product.to_entity()
            except NoResultFound:
                return None
