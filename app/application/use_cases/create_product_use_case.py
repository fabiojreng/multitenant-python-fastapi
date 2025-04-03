from app.domain.interfaces.iproduct_repository import ProductRepositoryInterface
from app.domain.interfaces.use_case_interface import UseCaseInterface
from app.infra.models.product_orm import ProductORM


class CreateProductUseCase(UseCaseInterface):
    def __init__(self, repository: ProductRepositoryInterface):
        self.__repository = repository

    def execute(self, params: dict = None) -> dict:
        produto = ProductORM(name=params["name"])
        return self.__repository.create(produto)
