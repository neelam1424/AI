from fastapi import FastAPI

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

