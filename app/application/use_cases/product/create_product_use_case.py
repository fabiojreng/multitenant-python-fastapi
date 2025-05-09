from app.domain.entities.product import Product
from app.domain.entities.stock_movements import StockMovement
from app.domain.interfaces.entities.iproduct_repository import ProductRepositoryInterface
from app.domain.interfaces.entities.istock_movements_repository import StockMovementsRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_created, response_internal_error
from app.presentation.schemas.response_schema import SchemaResponseHttp


class CreateProductUseCase(UseCaseInterface):
    def __init__(self, product_repository: ProductRepositoryInterface,
                 stock_movements_repository: StockMovementsRepositoryInterface):
        self.__product_repository = product_repository
        self.__stock_movements_repository = stock_movements_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            product = Product.create(
                params["name"], params["image"], params["brand_id"], params["category_id"],
                params["supplier_id"], params["quantity"], params["price_cost"],
                params["selling_price"], params["quantity_min"], params["validate_date"]
            )
            self.__product_repository.create(product)

            movement_stock = StockMovement.create(
                product.get_product_id(), product.get_quantity(),
                None, "in"
            )

            self.__stock_movements_repository.create(movement_stock)

            return response_created(
                "Produto criado com sucesso",
                {
                    "id": product.get_product_id(),
                    "name": product.get_name()
                }
            )

        except:
            return response_internal_error("Erro inesperado ao criar o produto.")
