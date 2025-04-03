from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from fastapi import Request
from app.domain.interfaces.idatabase import ConnectionDBInterface


load_dotenv()

DATABASE_URL = (f"postgresql://"
                f"{os.getenv('DB_USER')}:"
                f"{os.getenv('DB_PASSWORD')}"
                f"@{os.getenv('DB_HOST')}:"
                f"{os.getenv('DB_PORT')}"
                f"/{os.getenv('DB_NAME')}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)



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
