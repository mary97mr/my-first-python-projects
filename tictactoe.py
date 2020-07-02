import numpy as np
from utils_tictactoe import make_a_move, print_game_board, change_turn, check_game, transform_matrix_to_tokens


def main():
    matrix_board = np.zeros((3, 3), dtype=np.int)
    turn = 1

    while True:

        token_list = transform_matrix_to_tokens(matrix_board)
        print_game_board(3, 3, token_list)
        coords = input(f"Player {turn}, give me a coordinate 'row,col' to place your piece: ")
        coords = coords.split(',')
        coords = list(map(int, coords))

        result = make_a_move(matrix_board, turn, coords[0], coords[1])
        if isinstance(result, int) and result == -1:
            continue

        matrix_board = result
        turn = change_turn(turn)
        result = check_game(matrix_board)

        if result == -1:
            print("It's a draw, nobody won, try again.")
            break
        elif result == 1 or result == 2:
            print(f"Player {result} won the game")
            break


if __name__ == "__main__":
    main()

