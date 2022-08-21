from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings
from app.src._base import models

def init_db(app: FastAPI)->None:
    register_tortoise(
    app,
    db_url=settings.DATABASE_URI,
    modules={"models": models.models},
    generate_schemas=True,
    add_exception_handlers=True,
)
    
async def close_db(app: FastAPI)->None:
    await Tortoise.close_connections()
    
