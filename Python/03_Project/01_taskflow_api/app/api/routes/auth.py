from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/signup", response_model=UserResponse)
def signup(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    user_repository = UserRepository(db)
    auth_service = AuthService(user_repository)

    return auth_service.signup(user_data)