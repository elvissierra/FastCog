from fastapi import APIRouter, status, Depends
from pydantic import EmailStr

from ..models.user_model import UserRegister, UserLogin, UserVerify, AccessToken, ResetPassword, RefreshToken, ConfirmForgotPassword
from ..services.auth_service import AuthService
from ..core.aws_cognito import AWS_Cognito
from ..core.dependencies import get_aws_cognito

auth_router = APIRouter(prefix="/api/v1/auth")

@auth_router.post("/register", status_code=status.HTTP_201_CREATED, tags=["Auth"])
async def register_user(user: UserRegister, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.user_signup(user, cognito)

""" User Register """
@auth_router.post('/register', status_code=status.HTTP_201_CREATED, tags=['Auth'])
async def signup_user(user: UserRegister, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.user_signup(user, cognito)


@auth_router.post('/verify_account', status_code=status.HTTP_200_OK, tags=["Auth"])
async def verify_account(
    data: UserVerify,
    cognito: AWS_Cognito = Depends(get_aws_cognito),
):
    return AuthService.verify_account(data, cognito)


""" Resend Conf Code """
@auth_router.post('/resend_confirmation_code', status_code=status.HTTP_200_OK, tags=['Auth'])
async def resend_confirmation_code(email: EmailStr, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.resend_confirmation_code(email, cognito)


""" User Login """
@auth_router.post('/signin', status_code=status.HTTP_200_OK, tags=["Auth"])
async def signin(data: UserLogin, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.user_signin(data, cognito)


""" Forgot Password """
@auth_router.post('/forgot_password', status_code=status.HTTP_200_OK, tags=["Auth"])
async def forgot_password(email: EmailStr, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.forgot_password(email, cognito)


""" Confirm Password """
@auth_router.post('/confirm_forgot_password', status_code=status.HTTP_200_OK, tags=["Auth"])
async def confirm_forgot_password(data: ConfirmForgotPassword, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.confirm_forgot_password(data, cognito)


""" Reset Password """
@auth_router.post('/change_password', status_code=status.HTTP_200_OK, tags=["Auth"])
async def change_password(data: ResetPassword, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.change_password(data, cognito)


""" Generate New Token """
@auth_router.post('/new_token', status_code=status.HTTP_200_OK, tags=["Auth"])
async def new_access_token(refresh_token: RefreshToken, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.new_access_token(refresh_token.refresh_token, cognito)


""" Logout """
@auth_router.post('/logout', status_code=status.HTTP_204_NO_CONTENT, tags=["Auth"])
async def logout(access_token: AccessToken, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.logout(access_token.access_token, cognito)


""" GET User """
@auth_router.get('/user_details', status_code=status.HTTP_200_OK, tags=["Auth"])
async def user_details(email: EmailStr, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.user_details(email, cognito)