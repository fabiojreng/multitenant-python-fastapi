from app.domain.interfaces.entities.icategory_repository import CategoryRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_ok, response_internal_error, response_not_found
from app.presentation.schemas.response_schema import SchemaResponseHttp


class FindCategoryIdUseCase(UseCaseInterface):
    def __init__(self, category_repository: CategoryRepositoryInterface) -> None:
        self.__category_repository = category_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            category = self.__category_repository.find_by_id(params)

            if not category:
                return response_not_found("Categoria não encontrada")

            return response_ok(
                "Categoria encontrada com sucesso",
                {
                    "category_id": category["category_id"],
                    "name": category["name"],
                    "description": category["description"],
                    "created_at": category["created_at"]

                }
            )

        except:
            return response_internal_error("Erro inesperado ao buscar a categoria.")
