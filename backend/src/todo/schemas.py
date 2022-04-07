from datetime import date
from fastapi_camelcase import CamelModel

from src.shared.schemas import ListResponse


class TodoBase(CamelModel):
    name: str
    deadline_date: date
    is_complete: bool = False


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True


class TodoList(ListResponse):
    results: list[Todo]
