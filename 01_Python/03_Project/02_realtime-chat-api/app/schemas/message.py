from datetime import datetime
from pydantic import BaseModel, Field


class MessageCreate(BaseModel):
    receiver_id: int = Field(..., gt=0)
    content: str = Field(..., min_length=1, max_length=1000)


class RoomMessageCreate(BaseModel):
    room_id: int = Field(..., gt=0)
    content: str = Field(..., min_length=1, max_length=1000)


class MessageResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int | None
    room_id: int | None
    content: str
    created_at: datetime

    class Config:
        from_attributes = True