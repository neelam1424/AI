<!-- 
Step 0: Understand the project problem
Step 1: Create project setup
Step 2: Setup PostgreSQL connection
Step 3: Setup SQLAlchemy Base + Session
Step 4: Setup Alembic
Step 5: Build User Signup
Step 6: Build Login
Step 7: Add JWT Auth
Step 8: Add Protected Route
Step 9: Build Workspace
Step 10: Build Project
Step 11: Build Task
Step 12: Assign Task
Step 13: Change Task Status
Step 14: Add RBAC
Step 15: Add tests


 -->


# TaskFlow API — Complete Learning Notes (Step 1 → Step 22)

# Goal

Build a professional Trello-like Task Management API while learning:

* PostgreSQL
* SQLAlchemy ORM
* Alembic
* Dependency Injection
* JWT Authentication
* Password Hashing
* Repository Pattern
* Service Layer
* RBAC (Role-Based Access Control)
* Clean Architecture

---

# Core Architecture

Every request follows this flow:

```text
Client Request
      |
      v
Route Layer
      |
      v
Dependency Injection
      |
      v
Service Layer
      |
      v
Repository Layer
      |
      v
SQLAlchemy ORM
      |
      v
PostgreSQL
      |
      v
Database Response
      |
      v
Repository
      |
      v
Service
      |
      v
Route
      |
      v
Pydantic Response Schema
      |
      v
JSON Response
```

---

# Clean Architecture Concepts

## Model

Represents database tables.

Example:

```python
class User(Base):
```

Maps to:

```sql
users table
```

---

## Schema

Validates request and response data.

Example:

```python
class UserCreate(BaseModel):
```

Used for:

```json
{
  "email": "test@gmail.com",
  "password": "secret123"
}
```

---

## Repository

Contains database queries.

Example:

```python
user_repository.get_by_email()
```

Repository only knows:

```text
CRUD
Database
Queries
```

Repository should NOT know:

```text
JWT
HTTP
Permissions
Business Rules
```

---

## Service

Contains business logic.

Example:

```python
AuthService.signup()
```

Service knows:

```text
Validation
Business Rules
Permissions
RBAC
```

---

## Route

HTTP Layer.

Example:

```python
@router.post("/signup")
```

Responsibilities:

```text
Receive Request
Call Service
Return Response
```

---

## Dependency

Reusable injected object.

Examples:

```python
Depends(get_db)
Depends(get_current_user)
Depends(get_task_service)
```

---

# Folder Structure

```text
app/
├── main.py

├── core/
│   ├── config.py
│   ├── security.py
│   ├── permissions.py
│   ├── roles.py
│   └── enums.py

├── db/
│   ├── session.py
│   └── base.py

├── api/
│   ├── dependencies.py
│   └── routes/
│       ├── auth.py
│       ├── workspace.py
│       ├── project.py
│       └── task.py

├── models/
│   ├── user.py
│   ├── workspace.py
│   ├── project.py
│   └── task.py

├── schemas/
│   ├── user.py
│   ├── workspace.py
│   ├── project.py
│   └── task.py

├── repositories/
│   ├── user_repository.py
│   ├── workspace_repository.py
│   ├── project_repository.py
│   └── task_repository.py

├── services/
│   ├── auth_service.py
│   ├── workspace_service.py
│   ├── project_service.py
│   └── task_service.py

└── tests/
```

---

# Database Design

## User

```text
id
full_name
email
hashed_password
role
is_active
created_at
```

---

## Workspace

```text
id
name
owner_id
created_at
```

Relationship:

```text
User
  |
  +----> Workspace
```

One user can own many workspaces.

---

## Project

```text
id
name
workspace_id
created_at
```

Relationship:

```text
Workspace
    |
    +----> Projects
```

One workspace can have many projects.

---

## Task

```text
id
title
description
status
project_id
assigned_to_id
created_at
```

Relationship:

```text
Project
   |
   +----> Tasks
```

---

# Overall Database Relationship

```text
User
 |
 +---- Workspace
           |
           +---- Project
                     |
                     +---- Task
```

Assignment relationship:

```text
User
 |
 +---- Assigned Tasks
```

---

# Authentication System

## Signup Flow

```text
POST /auth/signup
        |
        v
UserCreate Schema
        |
        v
AuthService.signup()
        |
        +--> Check email exists
        |
        +--> Hash password
        |
        v
UserRepository.create()
        |
        v
PostgreSQL
```

---

## Password Hashing

Plain password:

```text
mypassword123
```

Stored password:

```text
$2b$12$...
```

Functions:

```python
hash_password()
verify_password()
```

---

# Login Flow

```text
POST /auth/login
        |
        v
UserLogin Schema
        |
        v
AuthService.login()
        |
        +--> Find user
        |
        +--> Verify password
        |
        +--> Create JWT
        |
        v
Return Access Token
```

Response:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

---

# JWT Authentication

Token contains:

```json
{
  "sub": "user@email.com",
  "exp": "expiration"
}
```

Never store:

```text
Password
Hashed Password
Secrets
```

---

# Protected Route Flow

```text
Authorization Header
Bearer <token>
        |
        v
OAuth2PasswordBearer
        |
        v
get_current_user()
        |
        +--> Decode JWT
        |
        +--> Extract email
        |
        +--> Fetch user from DB
        |
        v
Current User Object
```

Example:

```python
current_user = Depends(get_current_user)
```

---

# Workspace Module

## Workspace Flow

```text
POST /workspaces
        |
        v
WorkspaceCreate
        |
        v
WorkspaceService
        |
        +--> owner_id = current_user.id
        |
        v
WorkspaceRepository
        |
        v
Database
```

---

## List Workspaces

```text
GET /workspaces
       |
       v
current_user.id
       |
       v
WorkspaceRepository.get_by_owner()
```

---

# Project Module

## Create Project Flow

```text
POST /projects
       |
       v
ProjectCreate
       |
       v
ProjectService
       |
       +--> Check workspace exists
       |
       +--> Check ownership
       |
       v
ProjectRepository.create()
```

---

## List Projects

```text
GET /projects/workspace/{id}
```

Flow:

```text
Workspace Exists?
       |
       v
User Owns Workspace?
       |
       v
Return Projects
```

---

# Task Module

## Create Task Flow

```text
POST /tasks
      |
      v
TaskCreate
      |
      v
TaskService
      |
      +--> Project Exists?
      |
      +--> Workspace Exists?
      |
      +--> User Owns Workspace?
      |
      v
TaskRepository.create()
```

Default Status:

```text
todo
```

---

## List Tasks

```text
GET /tasks/project/{project_id}
```

Flow:

```text
Project Exists
      |
      v
Workspace Exists
      |
      v
Ownership Check
      |
      v
Return Tasks
```

---

# Task Assignment

Endpoint:

```text
PATCH /tasks/{task_id}/assign
```

Request:

```json
{
  "user_id": 1
}
```

Flow:

```text
Task Exists?
      |
      v
Project Exists?
      |
      v
Workspace Exists?
      |
      v
Permission Check
      |
      v
Assigned User Exists?
      |
      v
Update assigned_to_id
```

---

# Task Status Update

Endpoint:

```text
PATCH /tasks/{task_id}/status
```

Allowed values:

```text
todo
in_progress
done
```

Flow:

```text
TaskStatusUpdate
       |
       v
Enum Validation
       |
       v
Task Exists?
       |
       v
Permission Check
       |
       v
Update Status
```

---

# Dependency Injection Flow

Database Dependency:

```python
db: Session = Depends(get_db)
```

Authentication Dependency:

```python
current_user: User = Depends(get_current_user)
```

Service Dependency:

```python
task_service: TaskService = Depends(get_task_service)
```

---

# Repository Pattern Flow

```text
Service
   |
   v
Repository
   |
   v
SQLAlchemy
   |
   v
PostgreSQL
```

Repository Responsibilities:

```text
Create
Read
Update
Delete
```

Repository Should NOT Handle:

```text
Permissions
JWT
Business Rules
HTTP Errors
```

---

# Service Layer Flow

```text
Route
   |
   v
Service
   |
   +--> Validation
   +--> Business Rules
   +--> Permissions
   +--> RBAC
   |
   v
Repository
```

Service Responsibilities:

```text
Ownership Checks
Role Checks
Business Decisions
```

---

# RBAC (Role-Based Access Control)

## Roles

```text
admin
manager
member
```

---

# Role Permissions

| Action             | Admin | Manager | Member |
| ------------------ | ----- | ------- | ------ |
| Create Workspace   | Yes   | Yes     | Yes    |
| Create Project     | Yes   | Yes     | No     |
| Create Task        | Yes   | Yes     | No     |
| Assign Task        | Yes   | Yes     | No     |
| Update Task Status | Yes   | Yes     | Yes    |

---

# RBAC Flow

```text
Request
   |
   v
JWT Authentication
   |
   v
Current User
   |
   v
require_roles()
   |
   +--> admin
   +--> manager
   +--> member
   |
   v
Allow / Deny
```

Helper:

```python
require_roles(
    current_user,
    ["admin", "manager"]
)
```

---

# HTTP Status Codes Used

## 200 OK

Success.

---

## 201 Created

Resource created.

---

## 400 Bad Request

Invalid input.

Example:

```text
Invalid task status
```

---

## 401 Unauthorized

Not authenticated.

Example:

```text
Invalid token
```

---

## 403 Forbidden

Authenticated but not allowed.

Example:

```text
Member trying to create project
```

---

## 404 Not Found

Resource doesn't exist.

Example:

```text
Task not found
```

---

# Key Professional Principles Learned

1. Models represent database tables.
2. Schemas validate request/response.
3. Repositories handle database access.
4. Services handle business logic.
5. Routes remain thin.
6. JWT handles authentication.
7. RBAC handles authorization.
8. Dependency Injection removes duplication.
9. Pydantic validates data before service logic.
10. Clean Architecture makes projects scalable.

# End of Phase 1

You now have a professional FastAPI backend containing:

* Authentication
* JWT Security
* PostgreSQL
* SQLAlchemy ORM
* Alembic
* Dependency Injection
* Repository Pattern
* Service Layer
* Workspace Management
* Project Management
* Task Management
* Task Assignment
* Status Updates
* RBAC
* Clean Architecture
