from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.repositories.workspace_repository import WorkspaceRepository
from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskAssign,
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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task_repository = TaskRepository(db)
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)
    user_repository = UserRepository(db)

    task_service = TaskService(
        task_repository=task_repository,
        project_repository=project_repository,
        workspace_repository=workspace_repository,
        user_repository=user_repository
    )

    return task_service.create_task(
        task_data=task_data,
        current_user=current_user
    )


@router.get("/project/{project_id}", response_model=List[TaskResponse])
def get_project_tasks(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task_repository = TaskRepository(db)
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)
    user_repository = UserRepository(db)

    task_service = TaskService(
        task_repository=task_repository,
        project_repository=project_repository,
        workspace_repository=workspace_repository,
        user_repository=user_repository
    )

    return task_service.get_project_tasks(
        project_id=project_id,
        current_user=current_user
    )


@router.patch("/{task_id}/assign", response_model=TaskResponse)
def assign_task(
    task_id: int,
    assign_data: TaskAssign,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task_repository = TaskRepository(db)
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)
    user_repository = UserRepository(db)

    task_service = TaskService(
        task_repository=task_repository,
        project_repository=project_repository,
        workspace_repository=workspace_repository,
        user_repository=user_repository
    )

    return task_service.assign_task(
        task_id=task_id,
        assign_data=assign_data,
        current_user=current_user
    )

@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_task_status(
    task_id: int,
    status_data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task_repository = TaskRepository(db)
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)
    user_repository = UserRepository(db)

    task_service = TaskService(
        task_repository=task_repository,
        project_repository=project_repository,
        workspace_repository=workspace_repository,
        user_repository=user_repository
    )

    return task_service.update_task_status(
        task_id=task_id,
        status_data=status_data,
        current_user=current_user
    )