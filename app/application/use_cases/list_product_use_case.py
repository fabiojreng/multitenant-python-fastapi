from app.domain.interfaces.iproduct_repository import ProductRepositoryInterface
from app.domain.interfaces.use_case_interface import UseCaseInterface


class ListProductsUseCase(UseCaseInterface):
    def __init__(self, repository: ProductRepositoryInterface):
        self.__repository = repository

    def execute(self, params: dict = None) -> dict:
        products = self.__repository.list_all()
        return {"products": products}
