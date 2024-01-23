from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import String, DateTime, func, ForeignKey

from database.db import Base

from app.models.users import UserModel
from app.models.anime import AnimeModel


class FavoritesModel(Base):
    __tablename__ = "favorites"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(AnimeModel.id, ondelete="CASCADE"), primary_key=True
    )
    anime_id: Mapped[int] = mapped_column(
        ForeignKey(UserModel.id, ondelete="CASCADE"), primary_key=True
    )
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())