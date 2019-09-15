from tic_tac_toe.utils import ai_input, is_real_player, is_win, print_board, usr_input


def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    x_move = True
    have_winner = False
    real_player = is_real_player()

    try:
        print_board(board)
        while 0 in sum(board, []):
            if real_player:
                row, col = usr_input("X" if x_move else "O")
            else:
                if x_move:
                    row, col = usr_input("X" if x_move else "O")
                else:
                    row, col = ai_input(board)

            if board[row - 1][col - 1] != 0:
                print(f'{"X" if board[row - 1][col - 1] == 1 else "O"} is here. Take another position.')
                continue

            board[row - 1][col - 1] = 1 if x_move else 2
            print_board(board)

            if is_win(board, 1 if x_move else 2):
                have_winner = True
                print(f'{"X" if x_move else "O"} win!')
                exit()

            x_move = not x_move
            # TODO: clear previous output
        if not have_winner:
            print('no one won :(')
    except (ValueError, IndexError) as error:
        print(error)
    except KeyboardInterrupt:
        print('\nexit...')
        exit()
