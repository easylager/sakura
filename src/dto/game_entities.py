from typing import Dict, Optional, List
from uuid import UUID

from pydantic import BaseModel, conint, Field


class BoardPoint(BaseModel):
    number: conint(ge=0, le=23)
    checkers_count: conint(ge=0, le=15)
    occupied_by: Optional[UUID] = None


class Board(BaseModel):
    bar_counts: Dict[UUID, int] = Field(..., description="Mapping of player UUIDs to their bar counts")
    points: List[BoardPoint]
