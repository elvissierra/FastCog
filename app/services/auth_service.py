from fastapi import HTTPException
from fastapi.responses import JSONResponse
import botocore

from ..core.aws_cognito import AWS_Cognito
from ..models.user_model import UserRegister

class AuthService:
    def user_register(user: UserRegister, cognito: AWS_Cognito):
        try:
            response = cognito.user_register(user)
        except botocore.exceptions.ClientError as e:
            if e.reponse["Error"]["Code"] == "UsernameExistsException":
                raise HTTPException(
                    status_code= 409, detail = "This email already has an associated account.")
            else:
                raise HTTPException(status_code= 500, detail= "Internal Server Error.")
        else:
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                content = {
                    "message": "User created successfully",
                    "sub": response["UserSub"]
                }
                return JSONResponse(content=content, sttus_code=201)
            
                