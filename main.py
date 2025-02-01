from fastapi import FastAPI
from app.routes.auth_route import auth_router

app.include_router(auth_router)
app = FastAPI(
    title= "FastCognito",
    description= "Authentication service powered by FastAPI and Cognito",
    version= "1.0.0",
)

@app.get("/")
def index():
    return {"message": "Authentication service"}