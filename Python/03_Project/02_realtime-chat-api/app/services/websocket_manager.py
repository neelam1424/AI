from fastapi import WebSocket


class WebSocketManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(
        self,
        user_id: int,
        websocket: WebSocket
    ):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(
        self,
        user_id: int
    ):
        self.active_connections.pop(user_id, None)

    def is_online(
        self,
        user_id: int
    ) -> bool:
        return user_id in self.active_connections

    async def send_personal_message(
        self,
        user_id: int,
        message: str
    ):
        websocket = self.active_connections.get(user_id)

        if websocket:
            await websocket.send_text(message)

    async def broadcast(
        self,
        message: str
    ):
        for websocket in self.active_connections.values():
            await websocket.send_text(message)