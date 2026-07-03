from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.repositories.room_repository import RoomRepository
from app.schemas.room import RoomCreate, RoomResponse


router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)


@router.post("/", response_model=RoomResponse)
async def create_room(
    room_data: RoomCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    room_repository = RoomRepository(db)

    return await room_repository.create_room(room_data.name)


@router.get("/", response_model=list[RoomResponse])
async def get_rooms(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    room_repository = RoomRepository(db)

    return await room_repository.get_all_rooms()