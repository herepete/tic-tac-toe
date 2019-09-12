def print_map(_map):
    result = ''
    for row in _map:
        for column in row:
            if column == 0:
                result += '[ ]'
            if column == 1:
                result += '[X]'
            if column == 2:
                result += '[O]'
        result += '\n'
    print(f'\r{result}')


def is_win(_map, player):
    r_combo = False
    c_combo = False
    rd_combo = False
    ld_combo = False

    for row in _map:
        if len(set(row)) == 1 and row.count(player) == 3:
            r_combo = True

    for column in list(zip(*_map)):
        if len(set(column)) == 1 and column.count(player) == 3:
            c_combo = True

    rd = [_map[i][i] for i in range(0, len(_map))]
    ld = [_map[i][~i] for i in range(0, len(_map))]

    rd_combo = len(set(rd)) == 1 and rd.count(player) == 3
    ld_combo = len(set(ld)) == 1 and ld.count(player) == 3

    return r_combo or c_combo or rd_combo or ld_combo



def main():
    _map = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    x_move = True
    have_winner = False

    try:
        while 0 in [item for sublist in _map for item in sublist]:
            row, column = list(map(int, input(f'{"X" if x_move else "O"} position: ').split()))
            if _map[row - 1][column - 1] != 0:
                print(f'{"X" if not x_move else "O"} is here. Take another position.')
                continue
            _map[row - 1][column - 1] = 1 if x_move else 2
            print_map(_map)
            if is_win(_map, 1 if x_move else 2):
                have_winner = True
                print(f'{"X" if x_move else "O"} win!')
                break
            x_move = not x_move
        if not have_winner:
            print('no one won :(')
    except ValueError as e:
        print(e)
