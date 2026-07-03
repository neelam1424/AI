from sqlalchemy.orm import Session

from app.models.task import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_by_id(self, task_id: int):
        return (
            self.db.query(Task)
            .filter(Task.id == task_id)
            .first()
        )

    def get_by_project(self, project_id: int):
        return (
            self.db.query(Task)
            .filter(Task.project_id == project_id)
            .all()
        )

    def update(self, task: Task):
        self.db.commit()
        self.db.refresh(task)
        return task