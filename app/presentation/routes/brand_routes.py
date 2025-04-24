from fastapi import APIRouter, Request

from app.application.use_cases.brand.create_brand_use_case import CreateBrandUseCase
from app.application.use_cases.brand.find_brand_id_use_case import FindBrandIdUseCase
from app.application.use_cases.brand.list_brands_use_case import ListBrandUseCase
from app.infra.repositories.postgreSQL.brand_repository import BrandRepository
from app.presentation.helpers.http_response_helper import http_response
from app.presentation.helpers.use_case_helper import get_use_case
from app.presentation.schemas.brand_schema import BrandCreateSchema
from app.presentation.schemas.response_schema import SchemaResponseHttp

router = APIRouter()


@router.post("/brand/", response_model=SchemaResponseHttp,
             responses={422: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
def create_brand(request: Request, brand_data: BrandCreateSchema):
    use_case = get_use_case(request, CreateBrandUseCase, BrandRepository)
    return http_response(use_case.execute(brand_data.model_dump()))


@router.get("/brand/{brand_id}", response_model=SchemaResponseHttp,
            responses={500: {"model": SchemaResponseHttp}})
def find_brand_by_id(request: Request, brand_id: str):
    use_case = get_use_case(request, FindBrandIdUseCase, BrandRepository)
    return http_response(use_case.execute(brand_id))


@router.get("/brands/", response_model=SchemaResponseHttp,
            responses={202: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
def list_brands(request: Request):
    use_case = get_use_case(request, ListBrandUseCase, BrandRepository)
    return use_case.execute()
