from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class AssignmentBase(BaseModel):
    name: str = Field(..., description="Assignment name")
    due_date: str = Field(..., description="Due date (YYYY-MM-DD)")
    points: int = Field(..., description="Total points possible")


class AssignmentCreate(AssignmentBase):
    """Creation payload for an Assignment."""
    pass


class AssignmentUpdate(BaseModel):
    """Partial update for an Assignment."""
    name: Optional[str] = None
    due_date: Optional[str] = None
    points: Optional[int] = None


class AssignmentRead(AssignmentBase):
    """Server representation returned to clients."""
    id: UUID = Field(default_factory=uuid4, description="Assignment ID")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
