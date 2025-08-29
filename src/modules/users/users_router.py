
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connection import get_async_db


from .deps import get_users_service, UsersService

users_router = APIRouter(
    prefix='/users',
    tags=["Users"]
)

@users_router.post('/')
async def create_user(
    payload,
    users_service: UsersService = Depends(get_users_service)
):
    pass

@users_router.patch('/{id}')
async def update_user():
    pass