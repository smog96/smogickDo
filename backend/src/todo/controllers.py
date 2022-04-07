from src.shared.router_generator import router_generator
from fastapi import Depends

from src.todo.schemas import Todo, TodoCreate, TodoList
from src.todo.services import TodoService

router = router_generator("todos", secured=False)


@router.get("/", response_model=TodoList)
async def fetch_all(
        skip: int = 0,
        limit: int = 100,
        service: TodoService = Depends(TodoService)
):
    data = await service.repo.all(skip, limit)
    return data


@router.post("/", response_model=Todo)
async def create(
        data: TodoCreate,
        service: TodoService = Depends(TodoService)
):
    return await service.repo.create(data)


@router.post("/{id}/complete", response_model=Todo)
async def complete(
        id: int,
        service: TodoService = Depends(TodoService)
):
    return await service.complete(id)



@router.post("/{id}/uncomplete", response_model=Todo)
async def un_complete(
        id: int,
        service: TodoService = Depends(TodoService)
):
    return await service.un_complete(id)
