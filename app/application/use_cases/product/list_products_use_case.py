from app.domain.interfaces.entities.iproduct_repository import ProductRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_internal_error, response_ok, response_no_content
from app.presentation.schemas.response_schema import SchemaResponseHttp


class ListProductsUseCase(UseCaseInterface):
    def __init__(self, repository: ProductRepositoryInterface):
        self.__repository = repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            products = self.__repository.list_all()

            # alterar depois para buscar produtos não ativos
            if not products:
                return response_no_content(
                    "Não há produtos disponíveis",
                )

            return response_ok(
                "Lista de produtos",
                {"produtos": products}
            )

        except Exception as e:
            return response_internal_error("Erro inesperado ao listar os produtos")
