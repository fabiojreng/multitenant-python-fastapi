from fastapi import APIRouter, Request

from app.application.use_cases.product.create_product_use_case import CreateProductUseCase
from app.application.use_cases.product.find_product_id_use_case import FindProductIdUseCase
from app.application.use_cases.product.list_products_use_case import ListProductsUseCase
from app.infra.repositories.postgreSQL.product_repository import ProductRepository
from app.infra.repositories.postgreSQL.stock_movements_repository import StockMovementsRepository
from app.presentation.helpers.http_response_helper import http_response
from app.presentation.helpers.use_case_helper import get_use_case
from app.presentation.schemas.product_schema import ProductCreateSchema
from app.presentation.schemas.response_schema import SchemaResponseHttp

router = APIRouter()


@router.get("/products/", response_model=SchemaResponseHttp,
            responses={202: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
def list_products(request: Request):
    use_case = get_use_case(request, ListProductsUseCase, ProductRepository)
    return http_response(use_case.execute())


@router.post("/product/", response_model=SchemaResponseHttp,
             responses={422: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
def create_product(request: Request, product_data: ProductCreateSchema):
    use_case = get_use_case(request, CreateProductUseCase, ProductRepository, StockMovementsRepository)
    return http_response(use_case.execute(product_data.model_dump()))


@router.get("/product/{product_id}", response_model=SchemaResponseHttp,
            responses={500: {"model": SchemaResponseHttp}})
def find_product_by_id(request: Request, product_id: str):
    use_case = get_use_case(request, FindProductIdUseCase, ProductRepository)
    return http_response(use_case.execute(product_id))
