from fastapi import WebSocket


class WebSocketManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}
        self.room_connections: dict[int, list[WebSocket]] = {}

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

    async def send_personal_json(
        self,
        user_id: int,
        data: dict
    ):
        websocket = self.active_connections.get(user_id)

        if websocket:
            await websocket.send_json(data)

    async def connect_to_room(
        self,
        room_id: int,
        websocket: WebSocket
    ):
        await websocket.accept()

        if room_id not in self.room_connections:
            self.room_connections[room_id] = []

        self.room_connections[room_id].append(websocket)

    def disconnect_from_room(
        self,
        room_id: int,
        websocket: WebSocket
    ):
        if room_id in self.room_connections:
            self.room_connections[room_id].remove(websocket)

            if len(self.room_connections[room_id]) == 0:
                del self.room_connections[room_id]

    async def send_room_json(
        self,
        room_id: int,
        data: dict
    ):
        connections = self.room_connections.get(room_id, [])

        for websocket in connections:
            await websocket.send_json(data)