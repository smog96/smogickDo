
from fastapi.routing import APIRouter
from src.core.config import settings


def router_generator(
    root_path: str, secured=settings.enable_auth, tags: list = None
) -> APIRouter:
    if settings.api_version[-1] == "/":
        raise ValueError(
            "Env var 'API_URL_PREFIX' mustn't end with '/'. For example: '/api_v2'"
        )

    if tags is None:
        # if tags are default
        tags = [root_path]

    if root_path[0] == "/":
        root_path = root_path[1:]

    dependencies = []

    # if secured:
    #    dependencies.append(is_authenticated)

    return APIRouter(
        prefix=f"{settings.api_version}/{root_path}",
        tags=tags,
        dependencies=dependencies,
    )
