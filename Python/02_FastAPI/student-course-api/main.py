from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

app = FastAPI()

# step 2 add pydantic schema

class StudentCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=100)
    course: str = Field(min_length=2, max_length=50)

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(default=None, gt=0, lt=100)
    course: Optional[str] = Field(default=None, min_length=2, max_length=50)

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    course: str

class StudentListResponse(BaseModel):
    count: int
    students: List[StudentResponse]



# Temporary database
students = []
student_id_counter = 1






@app.get("/")
def home():
    return {"message": "Student Course API is running"}


# 1:- Create Student - POST

#What is student?
# This is the request body sent by the client.

#What is StudentCreate?
# This means the incoming data must follow the structure of the StudentCreate Pydantic model.

@app.post(
        "/students",
        response_model = StudentResponse,
        status_code = status.HTTP_201_CREATED
          )
def create_student(student: StudentCreate):
    #I want to use and modify the global variable student_id_counter.
    # Without global, Python may think you are trying to create a new local variable inside the function.
    # We need this because every time a new student is created, we increase the counter.
    global student_id_counter

    #Create new student dictionary
    new_student = {
        "id": student_id_counter,
        "name": student.name,
        "email": student.email,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)
    student_id_counter += 1

    return {
        "message": "Student created succesfully",
        "student": new_student
    }

# 2:- Get all student -GET

@app.get(
        "/students",
        response_model=StudentListResponse,
        status_code = status.HTTP_200_OK

        )
def get_students():
    return{
        "count": len(students),
        "students": students
    }


# 3:- Get one student — Path parameter

@app.get(
        "/students/{student_id}",
        response_model = StudentResponse,
        status_code = status.HTTP_200_OK
        )
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )

# 4:- Search by course — Query parameter

@app.get(
        "/students/search",
        response_model=StudentListResponse,
        status_code=status.HTTP_200_OK
        )
def search_students(course: str):
    result = []

    for student in students:
        if student["course"].lower() == course.lower():
            result.append(student)
    
    return {
        "course": course,
        "count": len(result),
        "students": result
        }

# 5:- Update student — PUT

@app.put(
    "/students/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def update_student(student_id: int, updated_data: StudentUpdate):
    for student in students:
        if student["id"] == student_id:

            if updated_data.name is not None:
                student["name"] == updated_data.name

            if updated_data["email"] is not None:
                student["email"] = updated_data.email

            if updated_data.age is not None:
                student["age"] = updated_data.age

            if updated_data.course is not None:
                student["course"] = updated_data.course
            
            return {
                "message": "Student updated successfully",
                "student": student
            }
    HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


#5: Delete student - DELETE

@app.delete(
        "/students/{student_id}",
            status_code=status.HTTP_200_OK)
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            delete_student = students.pop(index)

            return {
                "message": "Student delete successfully",
                "student": delete_student
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )