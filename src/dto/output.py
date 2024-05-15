from pydantic import BaseModel, conint

from src.core.enums import GameWinType


class GameResultOutput(BaseModel):
    points: conint(ge=0)
    win_type: GameWinType
