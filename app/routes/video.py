from app.models.video import VideoModel
from app.schemas.video import VideoCreate, VideoGet, VideoDelete
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_async_session


video_app = APIRouter()



@video_app.get('/video/{video_id}', response_model=VideoGet)
async def video_get(video_id: int, 
                    session: AsyncSession = Depends(get_async_session)
):
    query = (
        select(VideoModel)
        .where(VideoModel.id == video_id)
    )
    exc = await session.execute(query)
    video_get = exc.fetchone()
    if video_get is not None:
        return video_get[0]
    else:
        raise HTTPException(404, "data not found")


@video_app.delete('/video/delete/{video_id}', response_model=VideoDelete)
async def delete_video(video_id: int,
                       session: AsyncSession = Depends(get_async_session)
    ):
    query = (
        delete(VideoModel)
        .where(VideoModel.id == video_id)
        .returning(VideoModel.id)
    )
    exc = await session.execute(query)
    await session.commit()
    video_del = exc.fetchone()
    if video_del is not None:
        return video_del[0]
    else:
        raise HTTPException(404, "data not found")


@video_app.post("/video/upload", response_model=VideoCreate)
async def create_video(video: VideoCreate, 
                       session: AsyncSession = Depends(get_async_session)
    ):
    video_post = VideoModel(**video.dict())
    session.add(video_post)
    await session.commit()

    return video
