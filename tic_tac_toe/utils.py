import sys
import random


def print_board(board):
    for row in board:
        print(''.join(f'[{" XO"[i]}]' for i in row))


def is_win(board, player):
    for row in board:
        if len(set(row)) == 1 and row.count(player) == 3:
            return True

    for column in list(zip(*board)):
        if len(set(column)) == 1 and column.count(player) == 3:
            return True

    r_diag = [board[i][i] for i in range(0, len(board))]
    if len(set(r_diag)) == 1 and r_diag.count(player) == 3:
        return True

    l_diag = [board[i][~i] for i in range(0, len(board))]
    if len(set(l_diag)) == 1 and l_diag.count(player) == 3:
        return True

    return False


def usr_input(prompt):
    while True:
        try:
            row, column = map(int, input(prompt).split())

            if row < 1 or row > 3 or column < 1 or column > 3:
                raise IndexError()

            return row, column
        except (ValueError, IndexError):
            print('Incorrect input. Try again. ')


def ai_input(board):
    while True:
        row, col = random.randint(1, 3), random.randint(1, 3)

        if board[row - 1][col - 1] != 0:
            continue

        return row, col


def is_real_player():
    if len(sys.argv) == 1:
        return True

    if 'ai' in sys.argv[1:]:
        return False

    return True
