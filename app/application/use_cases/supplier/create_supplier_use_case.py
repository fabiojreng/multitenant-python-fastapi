from app.domain.entities.supplier import Supplier
from app.domain.interfaces.entities.isupplier_repository import SupplierRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_internal_error, response_created, response_conflict
from app.presentation.schemas.response_schema import SchemaResponseHttp


class CreateSupplierUseCase(UseCaseInterface):
    def __init__(self, supplier_repository: SupplierRepositoryInterface):
        self.__supplier_repository = supplier_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            supplier_exists = self.__supplier_repository.find_by_email(params.get("email"))

            if supplier_exists:
                return response_conflict(
                    message="Fornecedor com este e-mail já existe.",
                    data={"email": params.get("email")}
                )

            supplier = Supplier.create(params.get("cod"), params.get("name"), params.get("document"),
                                       params.get("email"), params.get("phone"))

            self.__supplier_repository.create(supplier)

            return response_created(
                "Forncedor criado com sucesso",
                {
                    "id": supplier.get_supplier_id(),
                    "name": supplier.get_name(),
                }
            )

        except:
            return response_internal_error("Erro inesperado ao criar forncedor.")
