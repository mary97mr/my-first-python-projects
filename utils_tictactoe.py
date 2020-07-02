import numpy as np
import os
from typing import Union, List


def clear() -> None:
    """ Clear the terminal text. """
    os.system('cls')


def print_game_board(height: int, width: int, token_list: List[List[str]]) -> None:
    """ Prints game board according the height and width given.

    Args:
        height: Number of the rows in the board.
        width: Number of columns in the board.
        token_list: List of lists with the board information.
    """
    clear()

    for i in range(height):
        print_horizontal_line(width)
        print_vertical_line(width, token_list[i])

    print_horizontal_line(width)


def print_horizontal_line(size: int) -> None:
    """ Prints horizontal lines of the board.

    Args:
        size: Number of the columns of the board.
    """
    print(size * " ---")


def print_vertical_line(size: int, row_list: List[str]) -> None:
    """ Prints vertical lines of the board.

    Args:
        size: Number of the columns of the board.
        row_list: List with the token information of the board.
    """
    assert size == len(row_list)
    s = ""
    for i in range(size):
        s += f"| {row_list[i]} "
    print(s + "|")


def check_game(board_matrix: np.ndarray) -> int:
    """ Checks the status of the game.

    Args:
        board_matrix: Matrix with the board game information.

    Returns:
        0 if nobody won and there are empty spaces

        1 if player one won
        2 if player two won
        -1 if nobody won and there aren't empty spaces: draw
    """
    board_matrix_tr = np.transpose(board_matrix)
    board_matrix_d1 = board_matrix.diagonal()
    board_matrix_d2 = np.fliplr(board_matrix).diagonal()

    for r, c in zip(board_matrix, board_matrix_tr):
        if np.all(r == 1) or np.all(c == 1):
            return 1
        if np.all(r == 2) or np.all(c == 2):
            return 2

    if np.all(board_matrix_d1 == 1) or np.all(board_matrix_d2 == 1):
        return 1
    if np.all(board_matrix_d1 == 2) or np.all(board_matrix_d2 == 2):
        return 2

    if np.all(board_matrix):
        return -1
    else:
        return 0


def make_a_move(board_matrix: np.ndarray, player: int, row: int, col: int) -> Union[np.ndarray, int]:
    """ Makes a move and updates the given board matrix.

    Args:
        board_matrix: Matrix with the game board information.
        player: Number of the player that makes the move.
        row: Number with the row coordinate to update the board.
        col: Number with the column coordinate to update the board.

    Returns:
        Matrix with the updated game board information.
        -1 if invalid coordinates.
    """
    r = row - 1
    c = col - 1
    if r not in range(board_matrix.shape[0]) or c not in range(board_matrix.shape[1]) or board_matrix[r, c] != 0:
        print("Introduce valid coordinates.")
        return -1
    board_matrix[r, c] = player
    return board_matrix


def change_turn(turn: int) -> int:
    """ Switch turn in the game.
    Args:
         turn: Number of the player.
    """
    if turn == 1:
        return 2
    if turn == 2:
        return 1


def transform_matrix_to_tokens(matrix: np.ndarray) -> List[List[str]]:
    """ Transforms the matrix given to a list of lists replacing the numbers in strings(tokens).
    Args:
        matrix: matrix with the board information.

    Returns:
        A list of lists with the board information updated to tokens.

    """
    token_list = []

    for row in matrix:
        row_list = []
        for element in row:
            if element == 0:
                row_list.append(" ")
            elif element == 1:
                row_list.append("x")
            else:
                row_list.append("o")

        token_list.append(row_list)
    return token_list
