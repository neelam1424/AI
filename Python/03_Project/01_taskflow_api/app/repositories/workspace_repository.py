from sqlalchemy.orm import Session

from app.models.workspace import Workspace


class WorkspaceRepository:
    def __init__(self,db: Session):
        self.db = db


    def create(self, workspace: Workspace):
        self.db.add(workspace)
        self.db.commit()
        self.db.refresh(workspace)
        return workspace
    
    def get_by_id(self, workspace_id: int):
        return(
            self.db.query(Workspace)
            .filter(Workspace.id == workspace_id)
            .first()
        )
    def get_by_owner(self, owner_id: int):
        return(
            self.db.query(Workspace)
            .filter(Workspace.owner_id == owner_id)
            .all()
        )