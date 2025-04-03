from app.domain.interfaces.idatabase import ConnectionDBInterface
from app.domain.interfaces.iproduct_repository import ProductRepositoryInterface
from app.infra.models.product_orm import ProductORM


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface):
        self.__db = db

    def list_all(self) -> list[dict]:
        with self.__db.get_session() as session:
            products_orm = session.query(ProductORM).all()
            return products_orm

        # return [Product(id=p.id, name=p.name) for p in products_orm]

    def create(self, params: dict) -> dict:
        with self.__db.get_session() as session:
            session.add(params)
            session.commit()
            session.refresh(params)
        return {"id": params["id"], "name": params["name"]}
        # return Produto(id=produto.id, name=produto_orm.name)
