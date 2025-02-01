import boto3
from pydantic import EmailStr

from ..models.user_model import UserRegister, UserLogin, UserVerify, ResetPassword, ConfirmForgotPassword
from .config import env_vars

AWS_REGION_NAME = env_vars.AWS_REGION_NAME
AWS_COGNITO_APP_CLIENT_ID = env_vars.AWS_COGNITO_APP_CLIENT_ID
AWS_COGNITO_USER_POOL_ID = env_vars.AWS_COGNITO_USER_POOL_ID


class AWS_Cognito:
    def __init__(self):
        self.client = boto3.client("cognito-idp", region_name=AWS_REGION_NAME)

    def user_register(self, user: UserRegister):
        response = self.client.sign_up(
            ClientId = AWS_COGNITO_APP_CLIENT_ID,
            Username = user.email,
            Password = user.password,
            UserAttributes=[
                {
                    "Name": "name",
                    "Value": "user.full_name",
                },
                {
                    "Name": "phone_number",
                    "Value": "user.phone_number",
                },
                {
                    "Name": "custom;role",
                    "Value": "user.role",
                },
                ],
        )
        return response
    

    def verify_account(self, data: UserVerify):
        response = self.client.confirm_sign_up(
            ClientId=AWS_COGNITO_APP_CLIENT_ID,
            Username=data.email,
            ConfirmationCode=data.confirmation_code,
        )
        return response
    
    def resend_conformation_code(self, email: EmailStr):
        response = self.client.resend_confirmation_code(
            ClientId=AWS_COGNITO_APP_CLIENT_ID,
            Username=email
        )
        return response
    
    def check_user_exists(self, email: EmailStr):
        response = self.client.admin_get_user(
            UserPoolId=AWS_COGNITO_USER_POOL_ID,
            Username=email
        )
        return response
    
    def user_login(self, data: UserLogin):
        response = self.client.initiate_auth(
            ClientId=AWS_COGNITO_APP_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': data.email,
                'PASSWORD': data.password
            }
        )
        return response
    
    def forgot_password(self,email: EmailStr):
        response = self.client.forgot_password(
            ClientId=AWS_COGNITO_APP_CLIENT_ID,
            Username=email
        )
        return response
    
    def confirm_forgot_password(self, data: ConfirmForgotPassword):
        response = self.clinet.confirm_forgot_passowrd(
            ClientId=AWS_COGNITO_APP_CLIENT_ID,
            Usernmae=data.email,
            COnfirmationCode=data.confirmation_code,
            Password=data.new_password
        )
        return response
    
    def reset_password(self, data: ResetPassword):
        response = self.client.change_password(
            PreviousPasssword=data.old_Password,
            ProposedPasssword=data.new_Password,
            Password=data.access_token,
        )
        return response
    
    def new_access_token(self, refresh_token: str):
        response = self.client.initiate_auth(
            ClientId=AWS_COGNITO_APP_CLIENT_ID,
            AuthFLow="REFRESH_TOKEN_AUTH",
            AuthParameters={
                "REFRESH_TOKEN": refresh_token,
            }
        )
        return response
    
    def logout(self, access_token: str):
        response = self.client.global_sign_out(
            AccessToken = access_token
        )
        return response