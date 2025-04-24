from app.domain.entities.brand import Brand
from app.domain.interfaces.entities.ibrand_repository import BrandRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_internal_error, response_created
from app.presentation.schemas.response_schema import SchemaResponseHttp


class CreateBrandUseCase(UseCaseInterface):
    def __init__(self, repository: BrandRepositoryInterface):
        self.__repository = repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            brand = Brand.create(params.get("name"), params.get("description"))
            self.__repository.create(brand)
            return response_created(
                "Marca criada com sucesso",
                {
                    "id": brand.get_brand_id(),
                    "name": brand.get_name()
                }
            )

        except:
            return response_internal_error("Erro inesperado ao criar a marca.")
