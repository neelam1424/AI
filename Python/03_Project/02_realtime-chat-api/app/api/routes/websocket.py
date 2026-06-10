from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status

from app.core.security import decode_access_token
from app.db.session import AsyncSessionLocal
from app.repositories.user_repository import UserRepository
from app.services.manager_instance import websocket_manager
from app.services.user_status_service import UserStatusService


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