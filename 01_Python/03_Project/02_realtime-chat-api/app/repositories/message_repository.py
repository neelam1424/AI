from sqlalchemy import select, or_, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.message import Message


class MessageRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_direct_message(
        self,
        sender_id: int,
        receiver_id: int,
        content: str
    ) -> Message:
        message = Message(
            sender_id=sender_id,
            receiver_id=receiver_id,
            content=content
        )

        self.db.add(message)
        await self.db.commit()
        await self.db.refresh(message)

        return message

    async def create_room_message(
        self,
        sender_id: int,
        room_id: int,
        content: str
    ) -> Message:
        message = Message(
            sender_id=sender_id,
            room_id=room_id,
            content=content
        )

        self.db.add(message)
        await self.db.commit()
        await self.db.refresh(message)

        return message

    async def get_direct_conversation(
        self,
        user_one_id: int,
        user_two_id: int
    ) -> list[Message]:
        result = await self.db.execute(
            select(Message)
            .where(
                or_(
                    and_(
                        Message.sender_id == user_one_id,
                        Message.receiver_id == user_two_id
                    ),
                    and_(
                        Message.sender_id == user_two_id,
                        Message.receiver_id == user_one_id
                    )
                )
            )
            .order_by(Message.created_at.asc())
        )

        return list(result.scalars().all())

    async def get_room_messages(
        self,
        room_id: int
    ) -> list[Message]:
        result = await self.db.execute(
            select(Message)
            .where(Message.room_id == room_id)
            .order_by(Message.created_at.asc())
        )

        return list(result.scalars().all())