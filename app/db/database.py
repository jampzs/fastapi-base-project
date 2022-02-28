from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URI, echo=True, future=True)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Function to generate async connection to database.
    :return: AsyncSession - db session
    """
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
