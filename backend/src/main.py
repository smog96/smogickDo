from fastapi import FastAPI
from src.todo.controllers import router as todo_router

routers = (todo_router,)


def get_application() -> FastAPI:
    application = FastAPI()
    [application.include_router(_router) for _router in routers]
    return application


app = get_application()
