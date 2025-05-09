from app.domain.interfaces.entities.iproduct_repository import ProductRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_internal_error, response_ok, response_not_found
from app.presentation.schemas.response_schema import SchemaResponseHttp


class FindProductIdUseCase(UseCaseInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.__product_repository = product_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            product = self.__product_repository.find_by_id(params)

            if not product:
                return response_not_found("Produto não encontrado")

            return response_ok(
                "Produto encontrado com sucesso",
                {
                    "product_id": product["product_id"],
                    "name": product["name"],
                    "brand_id": product["brand_id"],
                    "category_id": product["category_id"],
                    "supplier_id": product["supplier_id"],
                    "quantity": product["quantity"],
                    "price_cost": product["price_cost"],
                    "selling_price": product["selling_price"],
                    "created_at": product["created_at"],
                    "status": product["status"],
                    "image": product["image"],
                    "quantity_min": product["quantity_min"],
                    "validate_date": product["validate_date"]
                }
            )
        except:
            return response_internal_error("Erro inesperado ao buscar o produto.")
