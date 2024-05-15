from fastapi import Body

from src.dto.input import GameResultInput
from src.services.game_process_services.evaluate_board_service import EvaluateBoardService


def get_evaluate_service(game_input: GameResultInput = Body(...)) -> EvaluateBoardService:
    return EvaluateBoardService(game_input)
