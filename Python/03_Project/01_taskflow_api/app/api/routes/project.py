from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.repositories.workspace_repository import WorkspaceRepository
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)

    project_service = ProjectService(
        project_repository=project_repository,
        workspace_repository=workspace_repository
    )

    return project_service.create_project(
        project_data=project_data,
        current_user=current_user
    )


@router.get("/workspace/{workspace_id}", response_model=List[ProjectResponse])
def get_workspace_projects(
    workspace_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)

    project_service = ProjectService(
        project_repository=project_repository,
        workspace_repository=workspace_repository
    )

    return project_service.get_workspace_projects(
        workspace_id=workspace_id,
        current_user=current_user
    )