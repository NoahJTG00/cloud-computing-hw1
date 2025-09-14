from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    name: str = Field(..., description="Course name")
    code: str = Field(..., description="Course code")
    credits: int = Field(..., description="Number of credits")


class CourseCreate(CourseBase):
    """Creation payload for a Course."""
    pass


class CourseUpdate(BaseModel):
    """Partial update for a Course."""
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None


class CourseRead(CourseBase):
    """Server representation returned to clients."""
    id: UUID = Field(default_factory=uuid4, description="Course ID")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
