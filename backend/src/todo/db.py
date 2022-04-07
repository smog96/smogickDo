from src.core.db.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Date, Boolean


class ToDoInstance(BaseModel):
    __tablename__ = "todos"
    __table_args__ = {"comment": "My ToDo list"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    deadline_date = Column(Date, nullable=True)
    is_complete = Column(Boolean, default=False)
