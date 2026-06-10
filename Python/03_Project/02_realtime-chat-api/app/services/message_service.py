from fastapi import HTTPException, status

from app.repositories.message_repository import MessageRepository
from app.repositories.user_repository import UserRepository
from app.schemas.message import MessageCreate, RoomMessageCreate


class MessageService:
    def __init__(
        self,
        message_repository: MessageRepository,
        user_repository: UserRepository
    ):
        self.message_repository = message_repository
        self.user_repository = user_repository

    async def send_direct_message(
        self,
        sender_id: int,
        message_data: MessageCreate
    ):
        receiver = await self.user_repository.get_by_id(
            message_data.receiver_id
        )

        if receiver is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Receiver not found"
            )

        if receiver.id == sender_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You cannot send message to yourself"
            )

        message = await self.message_repository.create_direct_message(
            sender_id=sender_id,
            receiver_id=message_data.receiver_id,
            content=message_data.content
        )

        return message

    async def send_room_message(
        self,
        sender_id: int,
        message_data: RoomMessageCreate
    ):
        message = await self.message_repository.create_room_message(
            sender_id=sender_id,
            room_id=message_data.room_id,
            content=message_data.content
        )

        return message

    async def get_direct_conversation(
        self,
        current_user_id: int,
        other_user_id: int
    ):
        other_user = await self.user_repository.get_by_id(other_user_id)

        if other_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        messages = await self.message_repository.get_direct_conversation(
            user_one_id=current_user_id,
            user_two_id=other_user_id
        )

        return messages

    async def get_room_messages(
        self,
        room_id: int
    ):
        messages = await self.message_repository.get_room_messages(room_id)

        return messages