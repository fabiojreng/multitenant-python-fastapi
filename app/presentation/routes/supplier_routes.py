from fastapi import APIRouter, Request

from app.application.use_cases.supplier.create_supplier_use_case import CreateSupplierUseCase
from app.application.use_cases.supplier.find_supplier_id_use_case import FindSupplierIdUseCase
from app.application.use_cases.supplier.list_suppliers_use_case import ListSupplierUseCase
from app.infra.repositories.postgreSQL.supplier_repository import SupplierRepository
from app.presentation.helpers.http_response_helper import http_response
from app.presentation.helpers.use_case_helper import get_use_case
from app.presentation.schemas.response_schema import SchemaResponseHttp
from app.presentation.schemas.supplier_schema import SupplierCreateSchema

router = APIRouter()


@router.post("/supplier/", response_model=SchemaResponseHttp,
             responses={409: {"model": SchemaResponseHttp}, 422: {"model": SchemaResponseHttp},
                        500: {"model": SchemaResponseHttp}})
def create_brand(request: Request, supplier_data: SupplierCreateSchema):
    use_case = get_use_case(request, CreateSupplierUseCase, SupplierRepository)
    return http_response(use_case.execute(supplier_data.model_dump()))


@router.get("/supplier/{supplier_id}", response_model=SchemaResponseHttp,
            responses={500: {"model": SchemaResponseHttp}})
def find_supplier_by_id(request: Request, supplier_id: str):
    use_case = get_use_case(request, FindSupplierIdUseCase, SupplierRepository)
    return http_response(use_case.execute(supplier_id))


@router.get("/suppliers/", response_model=SchemaResponseHttp,
            responses={202: {"model": SchemaResponseHttp}, 500: {"model": SchemaResponseHttp}})
def list_suppliers(request: Request):
    use_case = get_use_case(request, ListSupplierUseCase, SupplierRepository)
    return use_case.execute()
