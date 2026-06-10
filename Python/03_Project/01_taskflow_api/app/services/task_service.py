from fastapi import HTTPException, status

from app.models.task import Task
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.repositories.workspace_repository import WorkspaceRepository
from app.schemas.task import TaskCreate
from app.repositories.user_repository import UserRepository
from app.schemas.task import TaskCreate, TaskAssign


class TaskService:
    def __init__(
    self,
    task_repository: TaskRepository,
    project_repository: ProjectRepository,
    workspace_repository: WorkspaceRepository,
    user_repository: UserRepository
    ):
        self.task_repository = task_repository
        self.project_repository = project_repository
        self.workspace_repository = workspace_repository
        self.user_repository = user_repository

    def create_task(
        self,
        task_data: TaskCreate,
        current_user: User
    ):
        project = self.project_repository.get_by_id(task_data.project_id)

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )

        workspace = self.workspace_repository.get_by_id(project.workspace_id)

        if not workspace:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Workspace not found"
            )

        if workspace.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to create task in this project"
            )

        task = Task(
            title=task_data.title,
            description=task_data.description,
            project_id=task_data.project_id,
            status="todo"
        )

        return self.task_repository.create(task)

    def get_project_tasks(
        self,
        project_id: int,
        current_user: User
    ):
        project = self.project_repository.get_by_id(project_id)

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )

        workspace = self.workspace_repository.get_by_id(project.workspace_id)

        if not workspace:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Workspace not found"
            )

        if workspace.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to view tasks in this project"
            )

        return self.task_repository.get_by_project(project_id)
    def assign_task(
    self,
    task_id: int,
    assign_data: TaskAssign,
    current_user: User
):
        task = self.task_repository.get_by_id(task_id)

        if not task:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

        project = self.project_repository.get_by_id(task.project_id)

        if not project:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

        workspace = self.workspace_repository.get_by_id(project.workspace_id)

        if not workspace:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )

        if workspace.owner_id != current_user.id:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to assign this task"
        )

        assigned_user = self.user_repository.get_by_id(assign_data.user_id)

        if not assigned_user:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assigned user not found"
        )

        task.assigned_to_id = assign_data.user_id

        return self.task_repository.update(task)