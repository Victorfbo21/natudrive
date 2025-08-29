
from sqlalchemy.ext.asyncio import AsyncSession

from .users_repository import UsersRepository

class UsersService:
    
    def __init__(self, users_repository: UsersRepository, db_session: AsyncSession):
        self.users_repository = users_repository
        self.db_session = db_session
        
    async def create_user(self):
        pass
    
    async def update_user(self):
        pass