# WebSocket Manager in Python & FastAPI — Complete Beginner Guide

## What You Will Learn
- WebSockets
- HTTP vs WebSocket
- Real-time communication
- Connection management
- Async programming
- FastAPI WebSockets
- Broadcasting
- Personal messaging
- Chat application architecture

## Problem Statement

Build a WebSocket Manager that:
1. Accepts new WebSocket connections.
2. Stores connected clients.
3. Sends personal messages.
4. Broadcasts messages.
5. Removes disconnected clients.

## Why Build This?

This project teaches:
- Chat apps
- Live notifications
- Multiplayer games
- Real-time dashboards
- FastAPI WebSockets

## HTTP vs WebSocket

HTTP:

Client -> Request
Server -> Response
Connection closes

WebSocket:

Client <=======> Server

Connection stays open.

Both sides can send messages anytime.

## Core Idea

User connects
↓
Accept connection
↓
Store connection
↓
Receive messages
↓
Broadcast messages
↓
Remove disconnected users

## Algorithm

1. Create active_connections list.
2. Accept and store connections.
3. Remove disconnected users.
4. Send personal messages.
5. Broadcast messages to all users.
6. Handle disconnect events.

## WebSocket Manager Code

```python
class WebSocketManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message, websocket):
        await websocket.send_text(message)

    async def broadcast(self, message):
        for connection in self.active_connections:
            await connection.send_text(message)
```

## How It Works

### active_connections

Stores all connected users.

Example:

```python
[
    user1,
    user2,
    user3
]
```

### connect()

Accepts connection and stores websocket.

### disconnect()

Removes websocket from active_connections.

### send_personal_message()

Sends a message to one specific user.

### broadcast()

Loops through active connections and sends message to everyone.

## FastAPI Integration

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()
manager = WebSocketManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()

            await manager.broadcast(
                f"Message: {data}"
            )

    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

## Connection Lifecycle

Client Connects
↓
accept()
↓
Store WebSocket
↓
Receive Messages
↓
Broadcast Messages
↓
Client Disconnects
↓
Remove WebSocket

## Async Concepts

### async

Creates asynchronous function.

### await

Pauses current task and allows event loop to run other tasks.

## Time Complexity

Connect: O(1)

Disconnect: O(n)

Broadcast: O(number_of_connections)

## Space Complexity

O(number_of_connections)

## Common Mistakes

1. Forgetting await
2. Forgetting disconnect
3. Using HTTP endpoint instead of WebSocket endpoint

## Mental Model

Think of WebSocket Manager as a receptionist:

People enter → add them

People leave → remove them

Announcement arrives → send to everyone

## Resume Bullet

Built a FastAPI-style WebSocket Manager to maintain active client connections, support personal messaging and broadcasting, and enable real-time communication using asynchronous WebSocket endpoints.
