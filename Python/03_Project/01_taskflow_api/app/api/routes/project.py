from typing import List

from fastapi import APIRouter, Depends

from app.api.dependencies import get_current_user, get_project_service
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create_project(
    project_data: ProjectCreate,
    project_service: ProjectService = Depends(get_project_service),
    current_user: User = Depends(get_current_user)
):
    return project_service.create_project(
        project_data=project_data,
        current_user=current_user
    )


@router.get("/workspace/{workspace_id}", response_model=List[ProjectResponse])
def get_workspace_projects(
    workspace_id: int,
    project_service: ProjectService = Depends(get_project_service),
    current_user: User = Depends(get_current_user)
):
    return project_service.get_workspace_projects(
        workspace_id=workspace_id,
        current_user=current_user
    )