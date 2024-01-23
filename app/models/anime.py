from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import String, Text, DateTime, func, Date

from database.db import Base


class AnimeModel(Base):
    __tablename__ = "anime"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    genre: Mapped[str] = mapped_column(String(125))
    release_date: Mapped[Date] = mapped_column(Date, default=func.now(), onupdate=func.now())
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())