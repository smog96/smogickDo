from fastapi import Depends

from src.todo.repositories import TodoRepository


class TodoService:
    def __init__(self, repo: TodoRepository = Depends(TodoRepository)):
        self.repo = repo

    async def complete(self, id: int):
        return await self.repo.update(id, data={"is_complete": True})

    async def un_complete(self, id: int):
        return await self.repo.update(id, data={"is_complete": False})
