from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.room import Room


class RoomRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_room(
        self,
        name: str
    ) -> Room:
        room = Room(name=name)

        self.db.add(room)
        await self.db.commit()
        await self.db.refresh(room)

        return room

    async def get_by_id(
        self,
        room_id: int
    ) -> Room | None:
        result = await self.db.execute(
            select(Room).where(Room.id == room_id)
        )

        return result.scalar_one_or_none()

    async def get_all_rooms(self) -> list[Room]:
        result = await self.db.execute(
            select(Room).order_by(Room.id.asc())
        )

        return list(result.scalars().all())