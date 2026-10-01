from fastapi import APIRouter
from schema.user import CreateUser, LoginUser

from services.user import UserRegistration, UserLogin

router = APIRouter(prefix="/users", tags=["Users"])

# registration
@router.post("/registration")
def user_registration(newUser : CreateUser):
    return UserRegistration.registration_logic(newUser)

@router.post("/login")
def user_login(loginUser : LoginUser):
    return UserLogin.login_user(loginUser)