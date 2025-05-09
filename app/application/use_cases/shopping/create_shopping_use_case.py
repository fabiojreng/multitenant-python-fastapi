from app.domain.entities.shopping import Shopping
from app.domain.entities.stock_movements import StockMovement
from app.domain.interfaces.entities.ishopping_repository import ShoppingRepositoryInterface
from app.domain.interfaces.entities.istock_movements_repository import StockMovementsRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_created, response_internal_error
from app.presentation.schemas.response_schema import SchemaResponseHttp


class CreateShoppingUseCase(UseCaseInterface):
    def __init__(self, shopping_repository: ShoppingRepositoryInterface,
                 stock_movements_repository: StockMovementsRepositoryInterface):
        self.__shopping_repository = shopping_repository
        self.__stock_movements_repository = stock_movements_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            shopping = Shopping.create(
                supplier_id=params["supplier_id"],
                product_id=params["product_id"],
                price_cost=params["price_cost"],
                quantity=params["quantity"]
            )

            self.__shopping_repository.create(shopping)

            movement_stock = StockMovement.create(
                shopping.get_product_id(), shopping.get_quantity(),
                None, "in"
            )

            self.__stock_movements_repository.create(movement_stock)

            return response_created(
                "Compra registrada com sucesso",
                {
                    "shopping_id": shopping.get_shopping_id(),
                    "product_id": shopping.get_product_id()
                }
            )

        except Exception as e:
            print(e)
            return response_internal_error("Erro ao registrar compra.")
