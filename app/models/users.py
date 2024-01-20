from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import String, DateTime, func, LargeBinary, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.conf import Base
import uuid
from typing import Any

import bcrypt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel(Base):

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    _hashed_password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    @property
    def password(self):
        return self._hashed_password.decode("utf-8")

    @password.setter
    def password(self, password: str):
        self._hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, password: str):
        return pwd_context.verify(password, self.password)

    @classmethod
    async def find(cls, database_session: AsyncSession, where_conditions: list[Any]):
        _stmt = select(cls).where(*where_conditions)
        _result = await database_session.execute(_stmt)
        return _result.scalars().first()