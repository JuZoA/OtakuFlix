from sqlalchemy.ext.asyncio import (
                                    AsyncAttrs,
                                    AsyncEngine,
                                    AsyncSession,
                                    async_sessionmaker,
                                    create_async_engine,
                                )

from sqlalchemy.ext.declarative import declarative_base
from pathlib import PurePath
from typing import Final
from sqlalchemy import MetaData

_SQLALCHEMY_DATABASE_URL: Final[str] = "postgresql+asyncpg://postgres:qwerty@127.0..01:5432/OtakuFlix"

engine: Final[AsyncEngine] = create_async_engine(_SQLALCHEMY_DATABASE_URL)

async_session_maker: Final[async_sessionmaker[AsyncSession]] = async_sessionmaker(
    engine, expire_on_commit=False, autoflush=False, autocommit=False
)




Base = declarative_base()


