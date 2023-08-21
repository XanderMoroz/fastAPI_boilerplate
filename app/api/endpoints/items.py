from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.api.deps import get_db
from app.api.schemas.item import ItemCreate
from app.api.schemas.item import ItemSchema
from app.api.schemas.user import UserSchema
from app.db.cruds import crud_item

item_router = APIRouter()


@item_router.get("/items", response_model=List[ItemSchema], tags=["admin"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud_item.get_items(db=db, skip=skip, limit=limit)
    return items


@item_router.get("/users/me/items", response_model=List[ItemSchema])
def read_user_items(
    skip: int = 0,
    limit: int = 0,
    current_user: UserSchema = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    items = crud_item.get_user_items(db=db, user_id=current_user.id)
    return items


@item_router.post("/users/{user_id}/items", response_model=ItemSchema)
def create_item_for_user(item: ItemCreate, user_id: int, db: Session = Depends(get_db)):
    return crud_item.create_user_item(db=db, item=item, user_id=user_id)
