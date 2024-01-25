from fastapi_users import schemas
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar
from pydantic import BaseModel
from datetime import datetime
from fastapi import UploadFile, File

class VideoCreate(BaseModel):
    anime_id: int
    title: str
    file: str
    created_at: datetime
    updated_at: datetime

class VideoGet(BaseModel):
    id: int
    anime_id: int
    title: str

class VideoDelete(BaseModel):
    id: int