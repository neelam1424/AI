from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status

from app.core.security import decode_access_token
from app.db.session import AsyncSessionLocal
from app.repositories.user_repository import UserRepository
from app.services.manager_instance import websocket_manager
from app.services.user_status_service import UserStatusService
from app.repositories.message_repository import MessageRepository
from app.repositories.room_repository import RoomRepository

router = APIRouter(
    tags=["WebSocket"]
)


@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str
):
    payload = decode_access_token(token)

    if payload is None:
        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )
        return

    user_id = payload.get("sub")

    if user_id is None:
        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )
        return

    user_id = int(user_id)

    connected = False

    async with AsyncSessionLocal() as db:
        user_repository = UserRepository(db)
        user_status_service = UserStatusService(user_repository)

        try:
            await user_status_service.mark_online(user_id)

            await websocket_manager.connect(
                user_id=user_id,
                websocket=websocket
            )

            connected = True

            while True:
                data = await websocket.receive_text()

                await websocket_manager.send_personal_json(
                    user_id=user_id,
                    data={
                        "type": "echo",
                        "message": data
                    }
                )

        except WebSocketDisconnect:
            pass

        finally:
            if connected:
                websocket_manager.disconnect(user_id)
                await user_status_service.mark_offline(user_id)



@router.websocket("/ws/rooms/{room_id}")
async def room_websocket_endpoint(
    websocket: WebSocket,
    room_id: int,
    token: str
):
    payload = decode_access_token(token)

    if payload is None:
        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )
        return

    user_id = payload.get("sub")

    if user_id is None:
        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )
        return

    user_id = int(user_id)

    async with AsyncSessionLocal() as db:
        room_repository = RoomRepository(db)
        message_repository = MessageRepository(db)

        room = await room_repository.get_by_id(room_id)

        if room is None:
            await websocket.close(
                code=status.WS_1008_POLICY_VIOLATION
            )
            return

        await websocket_manager.connect_to_room(
            room_id=room_id,
            websocket=websocket
        )

        try:
            while True:
                content = await websocket.receive_text()

                message = await message_repository.create_room_message(
                    sender_id=user_id,
                    room_id=room_id,
                    content=content
                )

                await websocket_manager.send_room_json(
                    room_id=room_id,
                    data={
                        "type": "room_message",
                        "room_id": room_id,
                        "message": {
                            "id": message.id,
                            "sender_id": message.sender_id,
                            "room_id": message.room_id,
                            "content": message.content,
                            "created_at": str(message.created_at)
                        }
                    }
                )

        except WebSocketDisconnect:
            websocket_manager.disconnect_from_room(
                room_id=room_id,
                websocket=websocket
            )