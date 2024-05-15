from fastapi import APIRouter, Depends

from src.core.exc_handlers import exception_handler
from src.core.mappings import POINTS_MAPPING
from src.dependencies.service_dependencies import get_evaluate_service
from src.dto.output import GameResultOutput
from src.services.game_process_services.evaluate_board_service import EvaluateBoardService

game_router = APIRouter()


@game_router.post("/evaluate_game/", response_model=GameResultOutput)
def evaluate_game(
        service: EvaluateBoardService = Depends(get_evaluate_service),
        _=Depends(exception_handler)
):
    winner, game_type = service.evaluate_board()
    points = POINTS_MAPPING.get(game_type, 0)
    return GameResultOutput(points=points, win_type=game_type)
