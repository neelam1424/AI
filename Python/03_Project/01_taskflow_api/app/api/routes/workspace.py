from typing import List

from fastapi import APIRouter, Depends

from app.api.dependencies import get_current_user, get_workspace_service
from app.models.user import User
from app.schemas.workspace import WorkspaceCreate, WorkspaceResponse
from app.services.workspace_service import WorkspaceService


router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"]
)


@router.post("/", response_model=WorkspaceResponse)
def create_workspace(
    workspace_data: WorkspaceCreate,
    workspace_service: WorkspaceService = Depends(get_workspace_service),
    current_user: User = Depends(get_current_user)
):
    return workspace_service.create_workspace(
        workspace_data=workspace_data,
        current_user=current_user
    )


@router.get("/", response_model=List[WorkspaceResponse])
def get_my_workspaces(
    workspace_service: WorkspaceService = Depends(get_workspace_service),
    current_user: User = Depends(get_current_user)
):
    return workspace_service.get_my_workspaces(current_user)