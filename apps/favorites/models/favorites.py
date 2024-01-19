from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import String, DateTime, func, ForeignKey

from database.conf import Base

from anime.models.anime import Anime
from authentication.models.user import User

class Favorites(Base):
    favorite_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(Anime.id, ondelete="CASCADE"), primary_key=True
    )
    anime_id: Mapped[int] = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE"), primary_key=True
    )
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())