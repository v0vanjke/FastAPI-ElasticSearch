from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from api_v1.models import Base

SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/fastapi'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
