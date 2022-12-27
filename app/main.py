from fastapi import FastAPI
from .config import settings
from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# creates the initial database tables using the sqlalchemy models, instead of via alembic
#models.Base.metadata.create_all(bind=engine)

# fastapi instance
app = FastAPI()

# which domains can call the api
origins = ["*"]

# add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
    
# root
@app.get("/")
def root():
    return {"message": "This is a social media API to manage users and posts. \n created by Kevin October."}

