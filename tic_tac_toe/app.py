from typing import Optional

columns = {
    "A": 0,
    "B": 1,
    "C": 2
}


def validate_move(move):
    if len(move) != 2:
        raise ValueError("Move must be two characters (column and row)")
    col, row = move
    if col not in columns.keys():
        raise ValueError(f"Invalid column: {col}")
    try:
        row_num = int(row)
        if row_num < 1 or row_num > 3:
            raise ValueError(f"Invalid row: {row}")
        return col, row
    except ValueError:
        raise ValueError("Row must be a number between 1 and 3")


class Game:
    winner: Optional[str]
    current_player = 'X'
    turns: int = 0
    is_over = False
    grid: list[list[str]] = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    def play(self, move: str):
        try:
            column, row = validate_move(move)
            played = self.place(int(row) - 1, columns[column])
            if played:
                self.turns += 1
                self.switch_player()
            self.is_game_over()
        except ValueError as e:
            print(f"Invalid move: {e}")

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = "O"
        else:
            self.current_player = "X"

    def place(self, row: int, col: int) -> bool:
        if self.grid[row][col] == ' ' and col is not None:
            self.grid[row][col] = self.current_player
            return True
        else:
            print("position not empty")
            return False

    def is_game_over(self):
        if self.check_column_wins():
            return
        if self.check_row_wins():
            return
        if self.check_diagonal_wins():
            return
        if self.turns == 9:
            self.is_over = True
            self.winner = None

    def check_column_wins(self):
        for col in range(3):
            if (self.grid[0][col] == self.grid[1][col] ==
                    self.grid[2][col] != ' '):
                self.winner = self.grid[0][col]
                self.is_over = True
                return True
        return False

    def check_row_wins(self):
        for row in range(3):
            if (self.grid[row][0] == self.grid[row][1]
                    == self.grid[row][2] != ' '):
                self.winner = self.grid[row][0]
                self.is_over = True
                return True
        return False

    def check_diagonal_wins(self):
        if (self.grid[0][0] == self.grid[1][1]
                == self.grid[2][2] != ' '):
            self.winner = self.grid[0][0]
            self.is_over = True
            return True
        elif (self.grid[0][2] == self.grid[1][1]
              == self.grid[2][0] != ' '):
            self.winner = self.grid[0][2]
            self.is_over = True
            return True
        return False
