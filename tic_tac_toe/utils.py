import random
import sys


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


def pick_corner(board):
    if board[0][0] == 0:
        return 1, 1

    if board[0][2] == 0:
        return 1, 3

    if board[2][0] == 0:
        return 3, 1

    if board[2][2] == 0:
        return 3, 3

    raise ValueError()


def stop_win(board):
    xxo = [1, 1, 0]
    xox = [1, 0, 1]
    oxx = [0, 1, 1]

    if xxo in board:
        return board.index(xxo) + 1, 3

    if xox in board:
        return board.index(xox) + 1, 2

    if oxx in board:
        return board.index(oxx) + 1, 1

    if tuple(xxo) in list(zip(*board)):
        return 3, list(zip(*board)).index(tuple(xxo)) + 1

    if tuple(xox) in list(zip(*board)):
        return 2, list(zip(*board)).index(tuple(xox)) + 1

    if tuple(oxx) in list(zip(*board)):
        return 1, list(zip(*board)).index(tuple(oxx)) + 1

    r_diag = [board[i][i] for i in range(0, len(board))]
    l_diag = [board[i][~i] for i in range(0, len(board))]

    if xxo == r_diag:
        return 3, 3

    if oxx == r_diag:
        return 1, 1

    if xxo == l_diag:
        return 3, 1

    if oxx == l_diag:
        return 1, 3

    if xox in (r_diag, l_diag):
        return 2, 2

    raise ValueError()


def ai_win(board):
    oox = [2, 2, 0]
    oxo = [2, 0, 2]
    xoo = [0, 2, 2]

    if oox in board:
        return board.index(oox) + 1, 3

    if oxo in board:
        return board.index(oxo) + 1, 2

    if xoo in board:
        return board.index(xoo) + 1, 1

    if tuple(oox) in list(zip(*board)):
        return 3, list(zip(*board)).index(tuple(oox)) + 1

    if tuple(oxo) in list(zip(*board)):
        return 2, list(zip(*board)).index(tuple(oxo)) + 1

    if tuple(xoo) in list(zip(*board)):
        return 1, list(zip(*board)).index(tuple(xoo)) + 1

    r_diag = [board[i][i] for i in range(0, len(board))]
    l_diag = [board[i][~i] for i in range(0, len(board))]

    if oox == r_diag:
        return 3, 3

    if xoo == r_diag:
        return 1, 1

    if oox == l_diag:
        return 3, 1

    if xoo == l_diag:
        return 1, 3

    if oxo in (r_diag, l_diag):
        return 2, 2

    raise ValueError()


def ai_input(board):
    while True:
        try:
            return ai_win(board)
        except ValueError:
            pass

        try:
            row, col = pick_corner(board)
        except ValueError:
            row, col = random.randint(1, 3), random.randint(1, 3)

        if board[row - 1][col - 1] != 0:
            continue

        try:
            row, col = stop_win(board)
        except ValueError:
            pass

        return row, col


def is_real_player():
    if len(sys.argv) == 1:
        return True

    if 'ai' in sys.argv[1:]:
        return False

    return True
