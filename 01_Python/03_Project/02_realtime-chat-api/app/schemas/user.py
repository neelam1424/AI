from pydantic import BaseModel, EmailStr


class UserCreatte(BaseModel):
    name: str
    email: EmailStr 
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_online: bool

    class Config:
        from_attributes = True
        