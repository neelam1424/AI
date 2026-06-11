# Week 3 FastAPI Project

# Realtime Notification + Chat API

---

# Project Goal

Build a production-style realtime chat backend using FastAPI.

This project teaches:

* Async Programming
* Async Database Calls
* JWT Authentication
* Background Tasks
* WebSockets
* Realtime Notifications
* Room Chat
* Online/Offline Tracking
* Clean Architecture
* Repository Pattern
* Service Layer Pattern

---

# Final Features

## Authentication

* User Signup
* User Login
* JWT Access Tokens
* Protected Routes

## Messaging

* Direct Messages
* Room Messages
* Message History
* Message Storage

## Realtime

* WebSocket Connections
* Personal Notifications
* Room Chat
* Broadcast Notifications

## User Presence

* Online Status
* Offline Status

## Background Processing

* Email Notifications

---

# What We Are Building

A simplified version of:

* WhatsApp
* Slack
* Discord
* Microsoft Teams

---

# Core Architecture

```text
Client
   ↓
Routes
   ↓
Services
   ↓
Repositories
   ↓
Database
```

---

# Why This Architecture?

Bad:

```python
@app.post("/messages")
async def send_message():
    # validation
    # business logic
    # database logic
    # notifications
```

Everything is mixed together.

Good:

```text
Route
↓
Service
↓
Repository
↓
Database
```

Each layer has one responsibility.

---

# Project Structure

```text
app/

├── api/
│   ├── dependencies.py
│   └── routes/
│
├── core/
│   ├── config.py
│   └── security.py
│
├── db/
│   ├── session.py
│   └── base.py
│
├── models/
│
├── schemas/
│
├── repositories/
│
├── services/
│
└── main.py
```

---

# Database Architecture

Tables:

```text
users
messages
rooms
```

---

# User Table

Stores:

```text
id
name
email
hashed_password
is_online
```

Purpose:

```text
Authentication
User Management
Presence Tracking
```

---

# Message Table

Stores:

```text
id
sender_id
receiver_id
room_id
content
created_at
```

Purpose:

```text
Direct Messages
Room Messages
Chat History
```

---

# Room Table

Stores:

```text
id
name
```

Purpose:

```text
Group Chat
Room Management
```

---

# Authentication Flow

Signup:

```text
User submits data
↓
Validate request
↓
Hash password
↓
Store user
↓
Return user response
```

Login:

```text
User enters email/password
↓
Find user
↓
Verify password
↓
Generate JWT
↓
Return access token
```

Protected Route:

```text
Receive token
↓
Decode JWT
↓
Get user id
↓
Load user
↓
Allow access
```

---

# JWT Flow

Token Payload

```json
{
  "sub": "1",
  "exp": "timestamp"
}
```

Meaning:

```text
sub = user id
exp = expiration time
```

---

# Async Programming

Normal Function:

```python
def get_users():
```

Async Function:

```python
async def get_users():
```

Use async when waiting for:

```text
Database
HTTP Requests
Email
File Storage
WebSockets
```

---

# Event Loop

Think of event loop as:

```text
Task Manager
```

Example:

```text
Request A waits for database
↓
Event Loop handles Request B
↓
Database finishes
↓
Resume Request A
```

This is why FastAPI can handle many users efficiently.

---

# Async Database Flow

```text
Request
↓
AsyncSession
↓
SQL Query
↓
Database
↓
Result
```

Used:

```python
await db.execute(...)
```

---

# Repository Pattern

Repository contains:

```text
Database Queries Only
```

Example:

```python
UserRepository
MessageRepository
RoomRepository
```

Responsibilities:

```text
Insert Data
Update Data
Delete Data
Fetch Data
```

Repository must NOT:

```text
Contain business rules
Contain HTTP logic
Contain route logic
```

---

# Service Layer Pattern

Service contains:

```text
Business Logic
```

Example:

```python
MessageService
AuthService
NotificationService
```

Responsibilities:

```text
Validate rules
Coordinate repositories
Trigger notifications
```

Example:

```text
Check receiver exists
↓
Save message
↓
Send notification
```

---

# Message Sending Flow

```text
POST /messages/direct
↓
JWT identifies sender
↓
Service validates receiver
↓
Repository stores message
↓
Database commit
↓
Return saved message
```

---

# Background Tasks

Purpose:

Run slow tasks after response is returned.

Example:

```text
Email Notification
```

Without Background Task:

```text
Save Message
↓
Send Email
↓
Return Response
```

User waits.

With Background Task:

```text
Save Message
↓
Return Response
↓
Send Email Later
```

Much faster.

---

# Email Notification Flow

```text
Message Sent
↓
Receiver Offline
↓
Background Task Created
↓
Email Service Executes
```

---

# WebSocket Concepts

HTTP:

```text
Request
↓
Response
↓
Connection Closed
```

WebSocket:

```text
Connect
↓
Connection Stays Open
↓
Realtime Communication
```

---

# Why WebSockets?

Used for:

```text
Chat Apps
Notifications
Gaming
Stock Updates
Collaborative Tools
```

---

# WebSocket Manager

Purpose:

Track connected users.

Stores:

```python
active_connections
```

Example:

```python
{
    1: websocket,
    2: websocket
}
```

Meaning:

```text
User 1 Online
User 2 Online
```

---

# Personal Message Flow

```text
Receiver Connected
↓
Stored in active_connections
↓
Sender sends message
↓
Message saved
↓
Receiver found online
↓
WebSocket notification sent
```

---

# Offline Message Flow

```text
Receiver Offline
↓
Message saved
↓
Cannot find active connection
↓
Trigger email notification
```

---

# Secure WebSocket Authentication

Bad:

```text
/ws/1
```

Anyone can impersonate user 1.

Good:

```text
/ws?token=JWT
```

Flow:

```text
Receive JWT
↓
Decode JWT
↓
Get user id
↓
Connect authenticated user
```

---

# Online / Offline Tracking

On Connect:

```text
User opens WebSocket
↓
Mark is_online=True
```

On Disconnect:

```text
WebSocket closes
↓
Mark is_online=False
```

Stored in database.

---

# Room Chat Architecture

Room Connection Storage

```python
room_connections = {
    room_id: [
        websocket1,
        websocket2
    ]
}
```

Example:

```python
{
    1: [user1, user2],
    2: [user3]
}
```

---

# Room Message Flow

```text
User joins room
↓
WebSocket stored in room
↓
User sends message
↓
Message saved in DB
↓
Broadcast to all room members
```

---

# Broadcast Notifications

Purpose:

Send one message to all online users.

Examples:

```text
Server Maintenance
System Updates
Announcements
```

Flow:

```text
Create Notification
↓
WebSocket Manager
↓
Send to all active connections
```

---

# Notification Types

Direct Message

```json
{
  "type": "new_message"
}
```

Room Message

```json
{
  "type": "room_message"
}
```

Broadcast

```json
{
  "type": "broadcast_notification"
}
```

Room Join

```json
{
  "type": "user_joined_room"
}
```

Room Leave

```json
{
  "type": "user_left_room"
}
```

---

# End-to-End Direct Chat Flow

```text
Sender Login
↓
Receive JWT
↓
Send POST /messages/direct
↓
Validate Receiver
↓
Save Message
↓
Check Online Status
```

If Online:

```text
Send WebSocket Notification
```

If Offline:

```text
Send Email Notification
```

---

# End-to-End Room Chat Flow

```text
User Login
↓
Receive JWT
↓
Connect Room WebSocket
↓
Join Room
↓
Send Message
↓
Store Message
↓
Broadcast To Room
```

---

# What You Learned

Backend Architecture

```text
Routes
Services
Repositories
Schemas
Models
```

Authentication

```text
JWT
Password Hashing
Protected Routes
```

Async Programming

```text
async
await
event loop
async database
```

Realtime Communication

```text
WebSockets
Connection Manager
Realtime Messaging
```

Background Processing

```text
BackgroundTasks
Email Notifications
```

Group Communication

```text
Rooms
Broadcasts
Notifications
```

Professional Development Patterns

```text
Repository Pattern
Service Layer
Dependency Injection
Clean Architecture
```

---

# Current Project Status

Completed:

✅ Async Database Setup

✅ JWT Authentication

✅ User Management

✅ Direct Messaging

✅ Room Messaging

✅ Background Email Notifications

✅ WebSocket Manager

✅ Secure WebSocket Authentication

✅ Online/Offline Tracking

✅ Broadcast Notifications

Next:

```text
Part 11
Middleware + Custom Exception Handlers

Part 12
File Uploads

Part 13
Testing with Pytest

Part 14
TestClient & HTTPX

Part 15
Mocking Dependencies
```
