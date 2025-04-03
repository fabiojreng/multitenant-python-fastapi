import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infra.fake_db.base import Base
from app.infra.fake_db.supplier_model import SupplierORM
from app.infra.fake_db.product_model import ProductORM


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    Base.metadata.drop_all(bind=engine)
    session.close()
