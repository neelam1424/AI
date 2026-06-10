from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.models import user, message, room


app = FastAPI(
    title="Realtime Notification + Chat API"
)


@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
async def health_check():
    return {"status": "ok"}