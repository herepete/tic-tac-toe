from tic_tac_toe.utils import is_real_player, is_win, print_board, user_input


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
