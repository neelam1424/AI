from fastapi import APIRouter, Depends

from app.api.dependencies import get_auth_service, get_current_user
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse, Token
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/signup", response_model=UserResponse)
def signup(
    user_data: UserCreate,
    auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.signup(user_data)


@router.post("/login", response_model=Token)
def login(
    login_data: UserLogin,
    auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.login(login_data)


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user