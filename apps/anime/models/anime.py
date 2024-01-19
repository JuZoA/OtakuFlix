from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import String, Text, DateTime, func, Date

from database.conf import Base


class Anime(Base):
    anime_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    genre: Mapped[str] = mapped_column(String(125))
    release_date: Mapped[Date] = mapped_column(Date, default=func.now(), onupdate=func.now())
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())