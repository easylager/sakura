from typing import Tuple, Optional
from uuid import UUID

from src.core.enums import GameWinType
from src.dto.game_entities import Board
from src.dto.input import GameResultInput


class EvaluateBoardService:
    """
    A service class to evaluate the outcome of a short backgammon game.
    The service determines the winner and the type of win (oin, mars, koks)
    based on the board state and the individual starting positions of each player.

    Attributes:
        board (Board): An instance of Board containing the current state of the game.
        start_position (Dict[UUID, int]): A dictionary mapping each player's UUID to their starting position on the board.
    """

    def __init__(self, game_input: GameResultInput):
        """
        Initializes the EvaluateBoardService with the game board and starting positions.

        Parameters:
            game_input (GameResultInput): The game input containing the board and starting positions.
        """
        self.board = game_input.board
        self.start_position = game_input.start_position

    def evaluate_board(self) -> Tuple[UUID, GameWinType]:
        """
        Evaluates the board to determine the winner and the type of victory based on the current state of the game.

        Returns:
            Tuple[UUID, GameWinType]: The UUID of the winner and the type of win (oin, mars, koks).

        Raises:
            ValueError: If no winner can be determined based on the current board state.
        """
        players = list(self.board.bar_counts.keys())
        player1, player2 = players[0], players[1]

        winner = self.determine_winner(player1, player2)
        if not winner:
            raise ValueError("No winner can be determined from the current board state.")

        loser = player2 if winner == player1 else player1
        game_type = self.determine_game_type(loser)
        return winner, game_type

    def determine_winner(self, player1: UUID, player2: UUID) -> Optional[UUID]:
        """
        Determines which player has won by checking if all checkers are off the board.

        Parameters:
            player1 (UUID): UUID of the first player.
            player2 (UUID): UUID of the second player.

        Returns:
            Optional[UUID]: The UUID of the winning player or None if no winner is determined.
        """
        if self.all_checkers_off(player1):
            return player1
        elif self.all_checkers_off(player2):
            return player2
        return None

    def all_checkers_off(self, player_id: UUID) -> bool:
        """
        Checks if a player has all their checkers off the board, including no checkers on the bar.

        Parameters:
            player_id (UUID): UUID of the player to check.

        Returns:
            bool: True if all checkers of the player are off the board, False otherwise.
        """
        if self.board.bar_counts[player_id] > 0:
            return False
        total_checkers = sum(p.checkers_count for p in self.board.points if p.occupied_by == player_id)
        return total_checkers == 0

    def determine_game_type(self, loser: UUID) -> GameWinType:
        """
        Determines the type of victory based on the position of the loser's checkers.

        Parameters:
            loser (UUID): UUID of the losing player.

        Returns:
            GameWinType: The type of win (oin, mars, koks).
        """
        if self.has_checkers_on_bar_or_first_quarter(loser):
            return GameWinType.Koks
        elif self.has_checkers_outside_home(loser):
            return GameWinType.Mars
        else:
            return GameWinType.Oin

    def has_checkers_on_bar_or_first_quarter(self, player_id: UUID) -> bool:
        """
        Checks if the player has checkers on the bar or in their first quarter of the board.

        Parameters:
            player_id (UUID): UUID of the player to check.

        Returns:
            bool: True if the player has checkers on the bar or in their first quarter, False otherwise.
        """
        first_quarter_end = self.start_position[player_id] + 6 if self.start_position[player_id] + 6 <= 24 else 24
        return self.board.bar_counts[player_id] > 0 or self.checkers_in_zone(
            range(self.start_position[player_id], first_quarter_end), player_id) > 0

    def has_checkers_outside_home(self, player_id: UUID) -> bool:
        """
        Checks if the player has any checkers outside their home area (the six positions following their start).

        Parameters:
            player_id (UUID): UUID of the player to check.

        Returns:
            bool: True if the player has checkers outside the home area, False otherwise.
        """
        home_start = self.start_position[player_id] + 6
        home_end = 24  # end of the board
        return self.checkers_in_zone(range(home_start, home_end), player_id) > 0

    def checkers_in_zone(self, zone_range: range, player_id: UUID) -> int:
        """
        Counts the checkers within a specified zone for a given player.

        Parameters:
            zone_range (range): The range of board positions to check.
            player_id (UUID): UUID of the player whose checkers are to be counted.

        Returns:
            int: The number of checkers within the specified zone.
        """
        return sum(p.checkers_count for p in self.board.points if p.occupied_by == player_id and p.number in zone_range)
