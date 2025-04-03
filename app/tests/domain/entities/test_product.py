from datetime import date

from app.domain.entities.product import Product
from app.infra.fake_db.product_model import ProductORM
from app.presentation.schemas.product_schema import (
    ProductCreateSchema,
    ProductResponseSchema,
)


def test_create_and_restore_product(db):
    product_data = {
        "name": "Produto Teste",
        "brand_id": "teste123",
        "category_id": "teste456",
        "supplier_id": "teste789",
        "quantity": 10,
        "quantity_min": 2,
        "price_cost": 50,
        "selling_price": 100,
        "validate_date": date(2025, 1, 1),
    }

    schema_create = ProductCreateSchema(**product_data)

    product_entity = Product.create(
        name=schema_create.name,
        image=schema_create.image,
        brand_id=schema_create.brand_id,
        category_id=schema_create.category_id,
        supplier_id=schema_create.supplier_id,
        quantity=schema_create.quantity,
        price_cost=schema_create.price_cost,
        selling_price=schema_create.selling_price,
        quantity_min=schema_create.quantity_min,
        validate_date=schema_create.validate_date,
    )

    db_product = ProductORM(
        product_id=product_entity.product_id,
        name=product_entity.name,
        brand_id=product_entity.brand_id,
        category_id=product_entity.category_id,
        supplier_id=product_entity.supplier_id,
        quantity=product_entity.quantity,
        quantity_min=product_entity.quantity_min,
        price_cost=product_entity.price_cost.get_value(),
        selling_price=product_entity.selling_price.get_value(),
        validate_date=product_entity.validate_date,
        created_at=product_entity.created_at,
        status=product_entity.status.value,
    )

    db.add(db_product)
    db.commit()

    schema_response = ProductResponseSchema(**product_entity.to_dict())

    print(schema_response.model_dump_json)

    restored_product = db.query(ProductORM).filter_by(name="Produto Teste").first()

    product_restored_entity = Product.restore(
        product_id=restored_product.product_id,
        name=restored_product.name,
        quantity=restored_product.quantity,
        price_cost=restored_product.price_cost,
        selling_price=restored_product.selling_price,
        created_at=restored_product.created_at,
        status=restored_product.status,
        brand_id=restored_product.brand_id,
        category_id=restored_product.category_id,
        supplier_id=restored_product.supplier_id,
        image=restored_product.image,
        quantity_min=restored_product.quantity_min,
        validate_date=restored_product.validate_date,
    )

    assert product_restored_entity is not None
    assert product_restored_entity.product_id == product_entity.product_id
    assert product_restored_entity.name == product_entity.name
    assert (
            product_restored_entity.price_cost.get_value()
            == product_entity.price_cost.get_value()
    )
    assert (
            product_restored_entity.selling_price.get_value()
            == product_entity.selling_price.get_value()
    )
    assert product_restored_entity.status == product_entity.status
