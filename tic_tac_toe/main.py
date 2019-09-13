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


def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    x_move = True
    have_winner = False

    real_player = is_real_player()
    print(f'Real player: {real_player}.')

    try:
        while 0 in sum(board, []):
            row, column = user_input(f'{"X" if x_move else "O"} position: ')

            if board[row - 1][column - 1] != 0:
                print(f'{"X" if board[row - 1][column - 1] == 1 else "O"} is here. Take another position.')
                continue

            board[row - 1][column - 1] = 1 if x_move else 2
            print_board(board)

            if is_win(board, 1 if x_move else 2):
                have_winner = True
                print(f'{"X" if x_move else "O"} win!')
                exit()

            x_move = not x_move
            # TODO: clear previous output
        if not have_winner:
            print('no one won :(')
    except (ValueError, IndexError) as e:
        print(e)
    except KeyboardInterrupt:
        print('\nexit...')
        exit()
