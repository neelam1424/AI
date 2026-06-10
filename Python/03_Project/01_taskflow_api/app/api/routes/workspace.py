from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.repositories.workspace_repository import WorkspaceRepository
from app.schemas.workspace import WorkspaceCreate, WorkspaceResponse
from app.services.workspace_service import WorkspaceService


router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"]
)


@router.post("/", response_model=WorkspaceResponse)
def create_workspace(
    workspace_data: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    workspace_repository = WorkspaceRepository(db)
    workspace_service = WorkspaceService(workspace_repository)

    return workspace_service.create_workspace(
        workspace_data=workspace_data,
        current_user=current_user
    )


@router.get("/", response_model=List[WorkspaceResponse])
def get_my_workspaces(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    workspace_repository = WorkspaceRepository(db)
    workspace_service = WorkspaceService(workspace_repository)

    return workspace_service.get_my_workspaces(current_user)