from typing import Optional
from pydantic import BaseModel
from app.core.enums import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int


class TaskAssign(BaseModel):
    user_id: int


class TaskStatusUpdate(BaseModel):
    status: TaskStatus


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    project_id: int
    assigned_to_id: Optional[int]

    class Config:
        from_attributes = True