from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.domain.interfaces.entities.iproduct_repository import ProductRepositoryInterface
from app.infra.models.product_orm import ProductORM


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, db: ConnectionDBInterface):
        self.__db = db

    def list_all(self) -> list[dict]:
        with self.__db.get_session() as session:
            products_orm = session.query(ProductORM).all()
            products = []

            for product in products_orm:
                total_quantity = sum(s.quantity for s in product.shoppings)
                last_purchase = max((s.created_at for s in product.shoppings), default=None)

                product_data = product.to_entity()
                product_data.update({
                    "quantity": total_quantity,
                    "created_at": last_purchase
                })

                products.append(product_data)

            return products

    def create(self, params: dict) -> dict:
        model = ProductORM.from_entity(params)
        with self.__db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model.to_entity()

    def find_by_id(self, product_id: str) -> dict:
        with self.__db.get_session() as session:
            try:
                product = session.query(ProductORM).filter_by(product_id=product_id).one()

                total_quantity = sum(s.quantity for s in product.shoppings)
                last_purchase = max((s.created_at for s in product.shoppings), default=None)

                base = product.to_entity()
                base.update({
                    "quantity": total_quantity,
                    "created_at": last_purchase
                })

                return base

            except:
                return None
