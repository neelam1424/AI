from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    receiver_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    room_id: Mapped[int | None] = mapped_column(ForeignKey("rooms.id"), nullable=True)

    content: Mapped[str] = mapped_column(String(1000))
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    sender = relationship(
        "User",
        foreign_keys=[sender_id],
        back_populates="sent_messages"
    )

    receiver = relationship(
        "User",
        foreign_keys=[receiver_id],
        back_populates="received_messages"
    )