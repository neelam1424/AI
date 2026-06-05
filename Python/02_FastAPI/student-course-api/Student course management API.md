# Student Course Management API – FastAPI Learning Project

## Project Goal

This project is built to learn FastAPI fundamentals through a real CRUD API.

By building this project, we learn:

* FastAPI basics
* API development
* Routing
* Request lifecycle
* Pydantic validation
* Response models
* Status codes
* Exception handling
* CRUD operations

---

# What is an API?

API stands for:

Application Programming Interface

An API allows two applications to communicate with each other.

Example:

Client:

```text
Instagram Mobile App
```

Server:

```text
Instagram Backend
```

The mobile app sends requests.

The backend sends responses.

---

# What is FastAPI?

FastAPI is a modern Python web framework used to build APIs.

FastAPI provides:

* High performance
* Automatic validation
* Automatic API documentation
* Type safety
* Easy development experience

Example:

```python
from fastapi import FastAPI

app = FastAPI()
```

---

# What is JSON?

JSON stands for:

JavaScript Object Notation

It is the standard format used to exchange data between client and server.

Example:

```json
{
  "name": "Neelam",
  "age": 24
}
```

FastAPI receives JSON requests and returns JSON responses.

---

# Client vs Server

## Client

A client sends requests.

Examples:

* Browser
* Mobile App
* React Frontend
* Postman

Example:

```http
GET /students
```

---

## Server

A server receives requests and sends responses.

In this project:

```text
FastAPI Server
```

acts as the server.

---

# FastAPI Request Lifecycle

Whenever a request arrives:

```text
Client Request
      ↓
Route Matching
      ↓
Parameter Extraction
      ↓
Pydantic Validation
      ↓
Function Execution
      ↓
Response Validation
      ↓
JSON Serialization
      ↓
JSON Response
```

---

# What is a Route?

A route maps a URL to a Python function.

Example:

```python
@app.get("/students")
def get_students():
    pass
```

Meaning:

```text
GET /students
      ↓
Run get_students()
```

---

# HTTP Methods Used

## GET

Used to retrieve data.

Example:

```http
GET /students
```

---

## POST

Used to create data.

Example:

```http
POST /students
```

---

## PUT

Used to update data.

Example:

```http
PUT /students/1
```

---

## DELETE

Used to delete data.

Example:

```http
DELETE /students/1
```

---

# Project Features

This API supports:

* Create Student
* Get All Students
* Get Single Student
* Update Student
* Delete Student
* Search Student By Course

---

# Project Structure

Current Structure

```text
student-course-api/
│
├── main.py
```

As the project grows:

```text
app/
│
├── main.py
├── schemas.py
├── routes/
├── services/
├── models/
```

---

# Pydantic Schemas

Pydantic is used for:

* Validation
* Parsing
* Serialization

Example:

```python
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    course: str
```

FastAPI validates incoming data automatically.

---

# Request Schema

Used when creating a student.

```python
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    course: str
```

Example Request:

```json
{
  "name": "Neelam",
  "email": "neelam@example.com",
  "age": 24,
  "course": "FastAPI"
}
```

---

# Update Schema

Used for updating data.

```python
class StudentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]
    course: Optional[str]
```

Optional fields allow partial updates.

---

# Field Validation

Field validation ensures correct data.

Example:

```python
name: str = Field(min_length=3, max_length=50)
```

Rules:

```text
Minimum length = 3
Maximum length = 50
```

Age validation:

```python
age: int = Field(gt=0, lt=100)
```

Rules:

```text
Age > 0
Age < 100
```

---

# Response Models

Response models define what data is returned.

Example:

```python
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    course: str
```

Used as:

```python
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
```

Benefits:

* Cleaner responses
* Output validation
* Better API documentation

---

# In-Memory Database

This project stores data in:

```python
students = []
```

This acts as a temporary database.

Limitation:

```text
Data disappears when server restarts.
```

Later we will replace this with PostgreSQL.

---

# Create Student Flow

Route:

```python
@app.post("/students")
```

Request:

```json
{
  "name": "Neelam",
  "email": "neelam@example.com",
  "age": 24,
  "course": "FastAPI"
}
```

Flow:

```text
Request
 ↓
Pydantic Validation
 ↓
Student Object Created
 ↓
Stored in students list
 ↓
Response Returned
```

---

# Get Student Flow

Request:

```http
GET /students/1
```

Flow:

```text
Extract student_id
 ↓
Search list
 ↓
Return student
```

---

# Search Student Flow

Request:

```http
GET /students/search?course=FastAPI
```

Flow:

```text
Extract query parameter
 ↓
Filter students
 ↓
Return matching students
```

---

# Status Codes

Status codes tell the client what happened.

Common codes:

```text
200 OK
201 Created
404 Not Found
422 Validation Error
```

Example:

```python
status_code=status.HTTP_201_CREATED
```

Used when creating a student.

---

# HTTPException

Used for proper error handling.

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

Response:

```json
{
  "detail": "Student not found"
}
```

---

# Serialization

FastAPI converts Python objects into JSON.

Python:

```python
{
    "name": "Neelam"
}
```

JSON:

```json
{
    "name": "Neelam"
}
```

This process is called serialization.

---

# API Endpoints

## Home

```http
GET /
```

---

## Create Student

```http
POST /students
```

---

## Get All Students

```http
GET /students
```

---

## Get Student By ID

```http
GET /students/{student_id}
```

---

## Search Students

```http
GET /students/search?course=FastAPI
```

---

## Update Student

```http
PUT /students/{student_id}
```

---

## Delete Student

```http
DELETE /students/{student_id}
```

---

# Concepts Learned

By completing this project, we learned:

✓ FastAPI Fundamentals

✓ API Development

✓ JSON

✓ Client vs Server

✓ Request Lifecycle

✓ Routing

✓ Path Parameters

✓ Query Parameters

✓ Request Body

✓ Pydantic

✓ Validation

✓ Field Validation

✓ Response Models

✓ CRUD Operations

✓ Status Codes

✓ HTTPException

✓ Serialization

✓ Swagger Documentation

---

# Next Learning Steps

After this project:

1. FastAPI Project Structure
2. Dependency Injection
3. SQLAlchemy / SQLModel
4. PostgreSQL
5. Async FastAPI
6. Authentication (JWT)
7. File Uploads
8. Background Tasks
9. Middleware
10. Production Deployment

These concepts will transform this beginner CRUD API into a production-ready FastAPI application.
