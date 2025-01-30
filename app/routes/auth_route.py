from fastapi import APIRouter, status, Depends

from ..models.user_model import UserRegister
from ..services.auth_service import AuthService
from ..core.aws_cognito import AWS_Cognito
from ..core.dependencies import get_aws_cognito

auth_router = APIRouter(prefix="/api/v1/auth")

@auth_router.post("/register", status_code=status.HTTP_201_CREATED, tags=["Auth"])
async def register_user(user: UserRegister, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.user_signup(user, cognito)

