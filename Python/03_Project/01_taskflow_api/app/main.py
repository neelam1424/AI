from fastapi import FastAPI

from app.api.routes import auth, workspace, project,task

app =FastAPI(
    title = " TaskFlow API ",
    description=" A Trello-like Task MAnagement API ",
    version = "1.0.0"
)

app.include_router(auth.router)
app.include_router(workspace.router)
app.include_router(project.router)
app.include_router(task.router)


@app.get("/")
def root():
    return {"message": "TaskFlow API is running "}