from app.domain.interfaces.entities.isupplier_repository import SupplierRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_no_content, response_ok, response_internal_error
from app.presentation.schemas.response_schema import SchemaResponseHttp


class ListSupplierUseCase(UseCaseInterface):
    def __init__(self, supplier_repository: SupplierRepositoryInterface):
        self.__supplier_repository = supplier_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            suppliers = self.__supplier_repository.list_all()
            if not suppliers:
                return response_no_content("Não foi encontrado fornecedores cadastrados")

            return response_ok(
                "Lista de fornecedores",
                {
                    "forncedores": suppliers
                }
            )
        except:
            return response_internal_error("Erro inesperado ao listar os fornecedores")
