from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

#schema used for response
class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    email: EmailStr
    password: str
    

#schema used for response
class UserOut(BaseModel):
        id: int
        email: EmailStr
        created_at: datetime

        class Config:
            orm_model = True
        