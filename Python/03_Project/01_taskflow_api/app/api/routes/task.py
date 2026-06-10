from typing import List

from fastapi import APIRouter, Depends

from app.api.dependencies import get_current_user, get_task_service
from app.models.user import User
from app.schemas.task import (
    TaskAssign,
    TaskCreate,
    TaskResponse,
    TaskStatusUpdate
)
from app.services.task_service import TaskService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponse)
def create_task(
    task_data: TaskCreate,
    task_service: TaskService = Depends(get_task_service),
    current_user: User = Depends(get_current_user)
):
    return task_service.create_task(
        task_data=task_data,
        current_user=current_user
    )


@router.get("/project/{project_id}", response_model=List[TaskResponse])
def get_project_tasks(
    project_id: int,
    task_service: TaskService = Depends(get_task_service),
    current_user: User = Depends(get_current_user)
):
    return task_service.get_project_tasks(
        project_id=project_id,
        current_user=current_user
    )


@router.patch("/{task_id}/assign", response_model=TaskResponse)
def assign_task(
    task_id: int,
    assign_data: TaskAssign,
    task_service: TaskService = Depends(get_task_service),
    current_user: User = Depends(get_current_user)
):
    return task_service.assign_task(
        task_id=task_id,
        assign_data=assign_data,
        current_user=current_user
    )


@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_task_status(
    task_id: int,
    status_data: TaskStatusUpdate,
    task_service: TaskService = Depends(get_task_service),
    current_user: User = Depends(get_current_user)
):
    return task_service.update_task_status(
        task_id=task_id,
        status_data=status_data,
        current_user=current_user
    )