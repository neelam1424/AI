from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import SessionLocal

app = FastAPI(
    title = "TaskFlow API",
    description="A Trello-like Task Management API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "TaskFlow API is running"
    }


@app.get("/db-test")
def db_test():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
        return {"message": "Database connected successfully"}
    finally:
        db.close()

