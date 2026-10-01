# Import FastAPI class 

from fastapi import FastAPI

# imports routers in defferents modules
from api.routes.user import router as user_registration


# Create instance of FastAPi
app = FastAPI(title="Shop API")

# Routes
@app.get("/")
def home():
    return {"Message":"Welcome to Shop API"}


# registered using include_router() method
app.include_router(user_registration)