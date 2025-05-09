from fastapi import Request
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware

from app.infra.database.connection_postgreSQL import PostgresConnection
from app.presentation.http.response import as_json_response, response_bad_request, response_not_found, \
    response_internal_error

EXCLUDED_PATHS = {"/", "/docs", "/redoc", "/openapi.json"}


class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        tenant = request.headers.get("tenant")

        if request.url.path in EXCLUDED_PATHS:
            return await call_next(request)

        if not tenant:
            return as_json_response(response_bad_request("Tenant não passado no cabeçalho"))

        connection = PostgresConnection(request)

        try:
            engine = connection.get_engine()
            with engine.connect() as conn:
                schema_exists = conn.execute(
                    text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = :schema"),
                    {"schema": tenant}
                ).first()

                if not schema_exists:
                    return as_json_response(response_not_found("Tenant inválido ou schema não existe"))

            db_session = connection.connect()
            request.state.db = db_session
            print("conectou com o tenant")

            response = await call_next(request)


        except SQLAlchemyError as e:
            return as_json_response(response_internal_error("Erro de banco de dados"))

        except:
            return as_json_response(response_internal_error("Erro interno inesperado"))

        finally:
            connection.close()

        return response
