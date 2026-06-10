from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.services.manager_instance import websocket_manager


router = APIRouter(
    tags=["WebSocket"]
)


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: int
):
    await websocket_manager.connect(
        user_id=user_id,
        websocket=websocket
    )

    try:
        while True:
            data = await websocket.receive_text()

            await websocket_manager.send_personal_message(
                user_id=user_id,
                message=f"You said: {data}"
            )

    except WebSocketDisconnect:
        websocket_manager.disconnect(user_id)


@router.websocket("/ws-broadcast/{user_id}")
async def websocket_broadcast_endpoint(
    websocket: WebSocket,
    user_id: int
):
    await websocket_manager.connect(
        user_id=user_id,
        websocket=websocket
    )

    try:
        while True:
            data = await websocket.receive_text()

            await websocket_manager.broadcast(
                message=f"User {user_id}: {data}"
            )

    except WebSocketDisconnect:
        websocket_manager.disconnect(user_id)