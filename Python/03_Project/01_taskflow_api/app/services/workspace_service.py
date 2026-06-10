from app.models.workspace import Workspace
from app.models.user import User
from app.schemas.workspace import WorkspaceCreate
from app.repositories.workspace_repository import WorkspaceRepository


class WorkspaceService:
    def __init__(self, workspace_repository: WorkspaceRepository):
        self.workspace_repository = workspace_repository

    def create_workspace(
        self,
        workspace_data: WorkspaceCreate,
        current_user: User
    ):
        workspace = Workspace(
            name=workspace_data.name,
            owner_id=current_user.id
        )

        return self.workspace_repository.create(workspace)

    def get_my_workspaces(self, current_user: User):
        return self.workspace_repository.get_by_owner(current_user.id)