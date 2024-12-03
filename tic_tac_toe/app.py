from typing import Optional


class Game:
    winner: Optional[str]
    current_player = 'X'
    is_over = False
    grid: list[list[str]] = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    def play(self, move: str):
        pass
