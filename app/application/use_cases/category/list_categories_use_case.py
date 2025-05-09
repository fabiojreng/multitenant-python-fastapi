from app.domain.interfaces.entities.icategory_repository import CategoryRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_no_content, response_ok, response_internal_error
from app.presentation.schemas.response_schema import SchemaResponseHttp


class ListCategoriesUseCase(UseCaseInterface):
    def __init__(self, category_repository: CategoryRepositoryInterface):
        self.__category_repository = category_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            categories = self.__category_repository.list_all()
            if not categories:
                return response_no_content("Não foi encontrada categorias cadastradas")

            return response_ok(
                "Lista de categorias",
                {
                    "categories": categories
                }
            )
        except:
            return response_internal_error("Erro inesperado ao listar as categorias")
