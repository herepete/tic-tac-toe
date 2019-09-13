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

    rd = [board[i][i] for i in range(0, len(board))]
    if len(set(rd)) == 1 and rd.count(player) == 3:
        return True

    ld = [board[i][~i] for i in range(0, len(board))]
    if len(set(ld)) == 1 and ld.count(player) == 3:
        return True

    return False


def user_input(prompt):
    while True:
        try:
            row, column = map(int, input(prompt).split())

            if row < 1 or row > 3 or column < 1 or column > 3:
                raise IndexError()

            return row, column
        except (ValueError, IndexError):
            print('Incorrect input. Try again. ')


def is_real_player():
    if len(sys.argv) == 1:
        return True

    if 'ai' in sys.argv[1:]:
        return False

    return True
