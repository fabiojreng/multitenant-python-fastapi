from fastapi import APIRouter, Request

from app.application.use_cases.create_product_use_case import CreateProductUseCase
from app.application.use_cases.list_product_use_case import ListProductsUseCase
from app.infra.database.connection_postgreSQL import PostgresConnection
from app.infra.repositories.postgreSQL.product_repository import ProductRepository
from app.presentation.schemas.product_schema import ProductCreateSchema

router = APIRouter()


@router.get("/products/")
def list_products(request: Request):
    db_connection = PostgresConnection(request)
    repository = ProductRepository(db_connection)
    use_case = ListProductsUseCase(repository)

    return use_case.execute()


@router.post("/products/")
def create_product(request: Request, product_data: ProductCreateSchema):
    db_connection = PostgresConnection(request)
    repository = ProductRepository(db_connection)
    use_case = CreateProductUseCase(repository)

    return use_case.execute(product_data.model_dump())
