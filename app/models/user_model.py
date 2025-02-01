from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    full_name: str = Field(max_length=55)
    email: EmailStr
    phone_number: Annotated[str,MinLen(10)]
    password: Annotated[str, MinLen(7)]
    role: str

class UserVerify(BaseModel):
    email: EmailStr
    confirmation_code: Annotated[str, MaxLen(6)]

class UserLogin(BaseModel):
    email: EmailStr
    password: Annotated[str, MinLen(7)]

class ConfirmForgotPassword(BaseModel):
    email: EmailStr
    confirmation_code: Annotated[str, MaxLen(6)]
    new_password: Annotated[str, MinLen(7)]

class ResetPassword(BaseModel):
    old_password: Annotated[str, MinLen(7)]
    new_password: Annotated[str, MinLen(7)]
    access_token: str

class RefreshToken(BaseModel):
    refresh_token: str

class AccessToken(BaseModel):
    access_token: str