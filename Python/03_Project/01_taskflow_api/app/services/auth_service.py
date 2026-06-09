from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRespository
from app.core.security import hash_password


class AuthService:
    # as we call auth service we call the all database queries from repository
    def __init__(self, user_respository: UserRespository):
        self.user_respository = user_respository

    # we take schema as input as it validate the data
    #we have written get by email logic in 
    def signup(self, user_data: UserCreate):
        # 1:- check if there is already user with the same email id
        existing_user = self.user_data.get_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # 2:- Create User Object we use models

        new_user=User(
            full_name = user_data.full_name,
            email= user_data.email,
            hash_password = hash_password(user_data.password),
            role="member"
        )

        # 3:- Save user

        return self.user_respository.create(new_user)