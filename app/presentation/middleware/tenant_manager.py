from fastapi import Request
from sqlalchemy.exc import ProgrammingError, SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware

from app.infra.database.connection_postgreSQL import PostgresConnection

EXCLUDED_PATHS = {"/", "/docs", "/redoc", "/openapi.json"}


class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        tenant = request.headers.get("tenant")

        if request.url.path in EXCLUDED_PATHS:
            return await call_next(request)

        if not tenant:
            raise ValueError("Tenant not provided")

        connection = PostgresConnection(request)

        try:
            db_session = connection.connect()
            request.state.db = db_session
            print("conectou com o tenant")

            response = await call_next(request)

        except ProgrammingError:
            db_session.rollback()
            raise ValueError("Invalid tenant or schema does not exist")

        except SQLAlchemyError as e:
            db_session.rollback()
            raise ValueError(f"Database error: {str(e)}")

        finally:
            connection.close()

        return response
