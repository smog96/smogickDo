from src.core.repositories import CRUDRepository
from src.todo.db import ToDoInstance


class TodoRepository(CRUDRepository):
    model = ToDoInstance
