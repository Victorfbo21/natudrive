from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connection import get_async_db

from .users_repository import UsersRepository
from .users_service import UsersService


def get_users_repository(
    db_session: AsyncSession = Depends(get_async_db)    
) -> UsersRepository:
    return UsersRepository(db_session=db_session)


def get_users_service(
    users_repository: UsersRepository = Depends(get_users_repository),
    db_session: AsyncSession = Depends(get_async_db)
):
    return UsersService(
        users_repository=users_repository, 
        db_session=db_session
    )