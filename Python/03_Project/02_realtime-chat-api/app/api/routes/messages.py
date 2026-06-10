from fastapi import APIRouter, Depends, BackgroundTasks
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
from app.services.email_service import EmailService


router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post("/direct", response_model=MessageResponse)
async def send_direct_message(
    message_data: MessageCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    message_repository = MessageRepository(db)
    user_repository = UserRepository(db)
    email_service = EmailService()

    message_service = MessageService(
        message_repository=message_repository,
        user_repository=user_repository,
        email_service=email_service
    )

    return await message_service.send_direct_message(
        sender_id=current_user.id,
        message_data=message_data,
        background_tasks=background_tasks
    )