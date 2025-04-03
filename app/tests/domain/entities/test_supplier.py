import pytest
from datetime import datetime
from app.domain.entities.supplier import Supplier
from app.infra.fake_db.supplier_model import SupplierORM
from app.presentation.schemas.supplier_schema import (
    SupplierCreateSchema,
    SupplierResponseSchema,
)


def test_create_and_restore_supplier(db):
    supplier_data = {
        "cod": 123,
        "name": "Fornecedor Teste",
        "document": "12.345.678/0001-90",
        "email": "fornecedor@teste.com.br",
        "phone": "11 99999-9999",
    }

    schema_create = SupplierCreateSchema(**supplier_data)

    supplier_entity = Supplier.create(
        cod=schema_create.cod,
        name=schema_create.name,
        document=schema_create.document,
        email=schema_create.email,
        phone=schema_create.phone,
    )

    db_supplier = SupplierORM(
        supplier_id=supplier_entity.supplier_id,
        cod=supplier_entity.cod,
        name=supplier_entity.name.get_value(),
        document=supplier_entity.document.get_value(),
        email=supplier_entity.email.get_value(),
        phone=supplier_entity.phone,
        created_at=supplier_entity.created_at,
    )

    db.add(db_supplier)
    db.commit()

    schema_response = SupplierResponseSchema(**supplier_entity.to_dict())

    print(schema_response.model_dump_json)

    restored_supplier = db.query(SupplierORM).filter_by(name="Fornecedor Teste").first()

    supplier_restored_entity = Supplier.restore(
        supplier_id=restored_supplier.supplier_id,
        cod=restored_supplier.cod,
        name=restored_supplier.name,
        document=restored_supplier.document,
        email=restored_supplier.email,
        phone=restored_supplier.phone,
        created_at=restored_supplier.created_at,
    )

    assert supplier_restored_entity is not None
    assert supplier_restored_entity.supplier_id == supplier_entity.supplier_id
    assert supplier_restored_entity.cod == supplier_entity.cod
    assert supplier_restored_entity.name.get_value() == supplier_entity.name.get_value()
    assert (
        supplier_restored_entity.document.get_value()
        == supplier_entity.document.get_value()
    )
    assert (
        supplier_restored_entity.email.get_value() == supplier_entity.email.get_value()
    )
    assert supplier_restored_entity.phone == supplier_entity.phone
    # assert supplier_restored_entity.created_at == supplier_entity.created_at
