from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.workspace_repository import WorkspaceRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.services.auth_service import AuthService
from app.services.workspace_service import WorkspaceService
from app.services.project_service import ProjectService
from app.services.task_service import TaskService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user_repository = UserRepository(db)
    user = user_repository.get_by_email(email)

    if user is None:
        raise credentials_exception

    return user


def get_auth_service(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    return AuthService(user_repository)


def get_workspace_service(db: Session = Depends(get_db)):
    workspace_repository = WorkspaceRepository(db)
    return WorkspaceService(workspace_repository)


def get_project_service(db: Session = Depends(get_db)):
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)

    return ProjectService(
        project_repository=project_repository,
        workspace_repository=workspace_repository
    )


def get_task_service(db: Session = Depends(get_db)):
    task_repository = TaskRepository(db)
    project_repository = ProjectRepository(db)
    workspace_repository = WorkspaceRepository(db)
    user_repository = UserRepository(db)

    return TaskService(
        task_repository=task_repository,
        project_repository=project_repository,
        workspace_repository=workspace_repository,
        user_repository=user_repository
    )