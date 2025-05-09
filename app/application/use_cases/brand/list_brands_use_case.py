from app.domain.interfaces.entities.ibrand_repository import BrandRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_no_content, response_ok, response_internal_error
from app.presentation.schemas.response_schema import SchemaResponseHttp


class ListBrandUseCase(UseCaseInterface):
    def __init__(self, brand_repository: BrandRepositoryInterface):
        self.__brand_repository = brand_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            brands = self.__brand_repository.list_all()
            if not brands:
                return response_no_content("Não foi encontrada marcas cadastradas")

            return response_ok(
                "Lista de marcas",
                {
                    "brands": brands
                }
            )
        except:
            return response_internal_error("Erro inesperado ao listar as marcas")
