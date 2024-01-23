from fastapi import FastAPI
import uvicorn
from fastapi_users import fastapi_users, FastAPIUsers
from app.auth.auth import auth_backend
from app.schemas.user import UserRead, UserCreate
from app.models.users import UserModel
from app.auth.manager import get_user_manager
from app.routes.video import video_app

app = FastAPI(title="OtakuFlix")

fastapi_users = FastAPIUsers[UserModel, int](
    get_user_manager,
    [auth_backend]
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    video_app,
)