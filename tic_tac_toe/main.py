from tic_tac_toe.app import Game


def run():
    game = Game()
    while not game.is_over:
        print_grid(game.grid)
        move = input(f"\nEnter player {game.current_player} move (A1, A2, A3, B1, B2, ...):")
        game.play(move)
    print('Game over!')
    if game.winner:
        print(f'Winner is {game.winner}')
    else:
        print("It's a draw !")


def print_grid(grid: list[list[str]]):
    print('  | A | B | C |')
    for index, row in enumerate(grid):
        print(f'{index+1} | {" | ".join(row)} |')


if __name__ == '__main__':
    run()
