from app.domain.entities.category import Category
from app.domain.interfaces.entities.icategory_repository import CategoryRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_created, response_internal_error
from app.presentation.schemas.response_schema import SchemaResponseHttp


class CreateCategoryUseCase(UseCaseInterface):
    def __init__(self, category_repository: CategoryRepositoryInterface) -> None:
        self.__category_repository = category_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            category = Category.create(params.get("name"), params.get("description"))
            self.__category_repository.create(category)

            return response_created(
                "Categoria criada com sucesso",
                {
                    "id": category.get_category_id(),
                    "name": category.get_name()
                }
            )
        except:
            response_internal_error("Erro inesperado ao criar a categoria.")
