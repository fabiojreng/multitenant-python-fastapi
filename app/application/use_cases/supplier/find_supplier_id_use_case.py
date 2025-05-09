from app.domain.interfaces.entities.isupplier_repository import SupplierRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_ok, response_internal_error, response_not_found
from app.presentation.schemas.response_schema import SchemaResponseHttp

""


class FindSupplierIdUseCase(UseCaseInterface):
    def __init__(self, supplier_repository: SupplierRepositoryInterface) -> None:
        self.__supplier_repository = supplier_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            supplier = self.__supplier_repository.find_by_id(params)

            if not supplier:
                return response_not_found("Fornecedor não encontrado")

            return response_ok(
                "Fornecedor encontrado com sucesso",
                {
                    "supplier_id": supplier["supplier_id"],
                    "cod": supplier["cod"],
                    "name": supplier["name"],
                    "document": supplier["document"],
                    "email": supplier["email"],
                    "phone": supplier["phone"],
                    "created_at": supplier["created_at"]
                }
            )

        except:
            return response_internal_error("Erro inesperado ao buscar o fornecedor.")
