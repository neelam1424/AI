from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.repositories.message_repository import MessageRepository
from app.repositories.user_repository import UserRepository
from app.schemas.message import (
    MessageCreate,
    RoomMessageCreate,
    MessageResponse
)
from app.services.message_service import MessageService


router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post("/direct", response_model=MessageResponse)
async def send_direct_message(
    message_data: MessageCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    message_repository = MessageRepository(db)
    user_repository = UserRepository(db)

    message_service = MessageService(
        message_repository=message_repository,
        user_repository=user_repository
    )

    return await message_service.send_direct_message(
        sender_id=current_user.id,
        message_data=message_data
    )


@router.get("/direct/{other_user_id}", response_model=list[MessageResponse])
async def get_direct_conversation(
    other_user_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    message_repository = MessageRepository(db)
    user_repository = UserRepository(db)

    message_service = MessageService(
        message_repository=message_repository,
        user_repository=user_repository
    )

    return await message_service.get_direct_conversation(
        current_user_id=current_user.id,
        other_user_id=other_user_id
    )


@router.post("/room", response_model=MessageResponse)
async def send_room_message(
    message_data: RoomMessageCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    message_repository = MessageRepository(db)
    user_repository = UserRepository(db)

    message_service = MessageService(
        message_repository=message_repository,
        user_repository=user_repository
    )

    return await message_service.send_room_message(
        sender_id=current_user.id,
        message_data=message_data
    )


@router.get("/room/{room_id}", response_model=list[MessageResponse])
async def get_room_messages(
    room_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    message_repository = MessageRepository(db)
    user_repository = UserRepository(db)

    message_service = MessageService(
        message_repository=message_repository,
        user_repository=user_repository
    )

    return await message_service.get_room_messages(room_id)