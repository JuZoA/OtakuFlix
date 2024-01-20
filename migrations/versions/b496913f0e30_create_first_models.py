"""create first models

Revision ID: b496913f0e30
Revises: 
Create Date: 2024-01-20 12:04:52.828059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b496913f0e30'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animemodel',
    sa.Column('anime_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('genre', sa.String(length=125), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('anime_id')
    )
    op.create_table('usermodel',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favoritesmodel',
    sa.Column('favorite_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('anime_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['anime_id'], ['usermodel.user_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['animemodel.anime_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('favorite_id', 'user_id', 'anime_id')
    )
    op.create_table('videomodel',
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.Column('anime_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['anime_id'], ['animemodel.anime_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('video_id', 'anime_id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videomodel')
    op.drop_table('favoritesmodel')
    op.drop_table('usermodel')
    op.drop_table('animemodel')
    # ### end Alembic commands ###
