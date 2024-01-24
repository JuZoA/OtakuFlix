from fastapi_users import schemas
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar
from pydantic import BaseModel
from datetime import datetime
from datetime import date, datetime

class AnimeGet(BaseModel):
    id: int
    title: str
    description: str
    genre: str
    release_date:date
    created_at: datetime
    updated_at: datetime

class AnimeCreate(BaseModel):
    title: str
    description: str
    genre: str
    release_date:date
    created_at: datetime
    updated_at: datetime