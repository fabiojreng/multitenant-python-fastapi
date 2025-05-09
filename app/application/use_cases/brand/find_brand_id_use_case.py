from app.domain.interfaces.entities.ibrand_repository import BrandRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_ok, response_internal_error, response_not_found
from app.presentation.schemas.response_schema import SchemaResponseHttp


class FindBrandIdUseCase(UseCaseInterface):
    def __init__(self, brand_repository: BrandRepositoryInterface) -> None:
        self.__brand_repository = brand_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            brand = self.__brand_repository.find_by_id(params)

            if not brand:
                return response_not_found("Marca não encontrada")

            return response_ok(
                "Marca encontrada com sucesso",
                {
                    "brand_id": brand["brand_id"],
                    "name": brand["name"],
                    "description": brand["description"],
                    "created_at": brand["created_at"]

                }
            )

        except:
            return response_internal_error("Erro inesperado ao buscar a marca.")
