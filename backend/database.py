# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .config import settings

async_engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

async def init_db():
    # Create tables
    from .models import Base
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
