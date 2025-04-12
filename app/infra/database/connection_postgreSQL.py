import os

from dotenv import load_dotenv
from fastapi import Request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.domain.interfaces.database.idatabase import ConnectionDBInterface
from app.infra.database.base import Base

load_dotenv()

DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Base.metadata.create_all(bind=engine)


class PostgresConnection(ConnectionDBInterface):
    def __init__(self, request: Request):
        self.request = request
        self.db = None
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def connect(self):
        print("abrindo conexão")
        tenant = self.request.headers.get("tenant")
        print(tenant)

        self.db = self.SessionLocal()
        self.db.execute(text(f"SET search_path TO {tenant}"))
        self.db.commit()

        return self.db

    def close(self) -> None:
        if self.db:
            print("fechando conexão")
            self.db.close()
            self.db = None

    def get_session(self):
        return self.SessionLocal()
