from fastapi_users import schemas
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar
from pydantic import BaseModel
from datetime import datetime

class VideoCreate(BaseModel):
    anime_id: int
    title: str
    url: str
    created_at: datetime
    updated_at: datetime

class VideoGet(BaseModel):
    id: int
    anime_id: int
    title: str
    url: str

class VideoDelete(BaseModel):
    id: int