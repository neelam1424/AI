from fastapi import HTTPException, status

from app.models.project import Project
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.repositories.workspace_repository import WorkspaceRepository
from app.schemas.project import ProjectCreate


class ProjectService:
    def __init__(
        self,
        project_repository: ProjectRepository,
        workspace_repository: WorkspaceRepository
    ):
        self.project_repository = project_repository
        self.workspace_repository = workspace_repository

    def create_project(
        self,
        project_data: ProjectCreate,
        current_user: User
    ):
        workspace = self.workspace_repository.get_by_id(
            project_data.workspace_id
        )

        if not workspace:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Workspace not found"
            )

        if workspace.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to create project in this workspace"
            )

        project = Project(
            name=project_data.name,
            workspace_id=project_data.workspace_id
        )

        return self.project_repository.create(project)

    def get_workspace_projects(
        self,
        workspace_id: int,
        current_user: User
    ):
        workspace = self.workspace_repository.get_by_id(workspace_id)

        if not workspace:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Workspace not found"
            )

        if workspace.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to view projects in this workspace"
            )

        return self.project_repository.get_by_workspace(workspace_id)