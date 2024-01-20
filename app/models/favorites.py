from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import String, DateTime, func, ForeignKey

from database.conf import Base

from app.models.anime import AnimeModel
from app.models.users import UserModel

class FavoritesModel(Base):

    favorite_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(AnimeModel.anime_id, ondelete="CASCADE"), primary_key=True
    )
    anime_id: Mapped[int] = mapped_column(
        ForeignKey(UserModel.user_id, ondelete="CASCADE"), primary_key=True
    )
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())