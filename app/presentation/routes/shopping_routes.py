from fastapi import APIRouter, Request

from app.application.use_cases.shopping.create_shopping_use_case import CreateShoppingUseCase
from app.infra.repositories.postgreSQL.shopping_repository import ShoppingRepository
from app.infra.repositories.postgreSQL.stock_movements_repository import StockMovementsRepository
from app.presentation.helpers.http_response_helper import http_response
from app.presentation.helpers.use_case_helper import get_use_case
from app.presentation.schemas.response_schema import SchemaResponseHttp
from app.presentation.schemas.shopping_schema import ShoppingCreateSchema

router = APIRouter()


@router.post("/shopping/", response_model=SchemaResponseHttp,
             responses={422: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
def create_shopping(request: Request, shopping_data: ShoppingCreateSchema):
    use_case = get_use_case(request, CreateShoppingUseCase, ShoppingRepository, StockMovementsRepository)
    return http_response(use_case.execute(shopping_data.model_dump()))

# @router.get("/shoppings/", response_model=SchemaResponseHttp,
#             responses={202: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
# def list_shoppings(request: Request):
#     use_case = get_use_case(request, ListShoppingUseCase, ShoppingRepository)
#     return http_response(use_case.execute())
