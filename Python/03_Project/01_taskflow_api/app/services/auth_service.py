from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def signup(self, user_data: UserCreate):
        existing_user = self.user_repository.get_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        new_user = User(
            name=user_data.name,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
            # role="member"
        )

        return self.user_repository.create(new_user)