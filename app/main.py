from fastapi import FastAPI

from app.api.endpoints import items
from app.api.endpoints import users
from app.core.config import settings


tags_metadata = [
    {"name": "users", "description": "Operations with users"},
    {"name": "items", "description": "Operations with items"},
    {"name": "admin", "description": "Admin operations"},
    {"name": "auth", "description": "Authenticate operations"},
]

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_tags=tags_metadata,
    docs_url="/",
)


app.include_router(items.item_router, tags=["items"])
app.include_router(users.router)
