from fastapi import APIRouter, Request

from app.application.use_cases.category.create_category_use_case import CreateCategoryUseCase
from app.infra.repositories.postgreSQL.category_repository import CategoryRepository
from app.presentation.helpers.http_response_helper import http_response
from app.presentation.helpers.use_case_helper import get_use_case
from app.presentation.schemas.category_schema import CategoryCreateSchema
from app.presentation.schemas.response_schema import SchemaResponseHttp

router = APIRouter()


@router.post("/category/", response_model=SchemaResponseHttp,
             responses={422: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
def create_category(request: Request, category_data: CategoryCreateSchema):
    use_case = get_use_case(request, CreateCategoryUseCase, CategoryRepository)
    return http_response(use_case.execute(category_data.model_dump()))
