from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

# pydantic models
"""class Post(BaseModel):
    title: str
    content: str
    published: bool = True"""

# post request validation (Base class)
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# user input validation
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# validation for user info output
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    # reads arbitrary data sunch as a pydantic model as if it were a dict 
    class Config:
        orm_mode = True

# login validation
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# input validation for new posts
class PostCreate(PostBase):
    pass

# post output format model 
class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

# format of post with votes
class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

# token format
class Token(BaseModel):
    access_token: str
    token_type: str

# token payload data formatting
class TokenData(BaseModel):
    id: Optional[str] = None

# input data validation
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # number must be <= 1, (find better way to do this, RE?)