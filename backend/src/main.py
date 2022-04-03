from fastapi import FastAPI

routers = ()


def get_application() -> FastAPI:
    application = FastAPI()
    [application.include_router(_router) for _router in routers]
    return application


app = get_application()
