from pydantic import BaseModel

class CreateUser(BaseModel):
    name : str
    email : str
    password : str
    birthday : str
    role : str

class LoginUser(BaseModel):
    email : str
    password : str
