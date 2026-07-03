from sqlalchemy.orm import declarative_base

Base = declarative_base()

# from app.models.user import User

# from app.models.user import User  # noqa
from app.models.workspace import Workspace  # noqa
from app.models.project import Project  # noqa
from app.models.task import Task  # noqa