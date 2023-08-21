from typing import List

from pydantic import BaseModel

from app.api.schemas.item import ItemSchema


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: int
    is_active: bool
    items: List[ItemSchema] = []

    class Config:
        orm_mode = True
