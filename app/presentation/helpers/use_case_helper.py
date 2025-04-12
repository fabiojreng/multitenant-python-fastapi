from fastapi import Request

from app.infra.database.connection_postgreSQL import PostgresConnection


def get_use_case(request: Request, use_case_class, *repository_classes):
    db_connection = PostgresConnection(request)
    repositories = [repo_class(db_connection) for repo_class in repository_classes]
    return use_case_class(*repositories)
