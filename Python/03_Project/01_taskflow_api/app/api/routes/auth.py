from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse, Token
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

from app.api.dependencies import get_current_user
from app.models.user import User


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

@router.post("/login", response_model=Token)
def login(
        login_data: UserLogin,
        db: Session = Depends(get_db)
):
    user_repository = UserRepository(db)
    auth_service = AuthService(user_repository)

    return auth_service.login(login_data)

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user