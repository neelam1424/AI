from typing import Optional
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int


class TaskAssign(BaseModel):
    user_id: int


class TaskStatusUpdate(BaseModel):
    status: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    project_id: int
    assigned_to_id: Optional[int]

    class Config:
        from_attributes = True