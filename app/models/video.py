from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import String, DateTime, func, ForeignKey

from database.conf import Base

from app.models.anime import AnimeModel


class VideoModel(Base):


    video_id: Mapped[int] = mapped_column(primary_key=True)
    anime_id: Mapped[int] = mapped_column(
        ForeignKey(AnimeModel.anime_id, ondelete="CASCADE"), primary_key=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())