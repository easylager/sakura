from typing import Dict
from uuid import UUID

from pydantic import BaseModel, Field

from src.dto.game_entities import Board


class GameResultInput(BaseModel):
    board: Board
    start_position: Dict[UUID, int] = Field(..., description="Mapping of player UUIDs to their starting positions")

    class Config:
        json_schema_extra = {
            "example": {
                "board": {
                    "bar_counts": {
                        "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0,
                        "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8": 0,
                        "12345678-90ab-cdef-1234-567890abcdef": 0
                    },
                    "points": [
                        {
                            "number": 0,
                            "checkers_count": 0,
                            "occupied_by": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                        }
                    ]
                },
                "start_position": {
                    "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0,
                    "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8": 0,
                    "12345678-90ab-cdef-1234-567890abcdef": 0
                }
            }
        }
