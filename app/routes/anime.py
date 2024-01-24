from app.models.anime import AnimeModel
from app.schemas.anime import AnimeGet, AnimeCreate
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_async_session


anime_app = APIRouter()

@anime_app.get("/anime/{anime_id}", response_model=AnimeGet)
async def anime_get(anime_id: int, 
                    session: AsyncSession = Depends(get_async_session)
                    ):
    query = (
        select(AnimeModel)
        .where(AnimeModel.id == anime_id)
    )
    exc = await session.execute(query)
    anime_get = exc.fetchone()
    if anime_get is not None:
        return anime_get[0]
    else: 
        raise HTTPException(404, "data not found")
    

@anime_app.post("/anime/uplaod")
async def anime_upload(anime: AnimeCreate, 
                       session: AsyncSession = Depends(get_async_session)
                       ):
    video_post = AnimeModel(**anime.dict())
    session.add(video_post)
    await session.commit()

    return anime