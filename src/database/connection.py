import os
from dotenv import load_dotenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()

if not DATABASE_URL:
    raise ValueError("Variavel de ambiente 'DATABASE_URL' não definida")


## Engine Assíncrono 
async_engine = create_async_engine(
    DATABASE_URL,
    echo = False,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=10,
    max_overflow=20
)

async_session_local = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

async def get_async_db():
    async with async_session_local() as session:
        try:
            yield session
        finally:
            await session.close()