from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

import settings

engine = create_async_engine(
    settings.DB_URL, 
    future=True, 
    echo=True, 
    execution_options={'isolation_level': 'AUTOCOMMIT'},
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db_session() -> Generator:
    try:
        session: AsyncSession = async_session
        yield session
    finally:
        session.close()

