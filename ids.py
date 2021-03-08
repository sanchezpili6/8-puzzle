from copy import deepcopy

def move_piece(board, direction, zero):
    if direction == 'up':
        board[zero[0]][zero[1]], board[zero[0]-1][zero[1]] = board[zero[0]-1][zero[1]], board[zero[0]][zero[1]]
    elif direction == 'down':
        board[zero[0]][zero[1]], board[zero[0]+1][zero[1]] = board[zero[0]+1][zero[1]], board[zero[0]][zero[1]]
    elif direction == 'right':
        board[zero[0]][zero[1]], board[zero[0]][zero[1] + 1] = board[zero[0]][zero[1]+1], board[zero[0]][zero[1]]
    elif direction == 'left':
        board[zero[0]][zero[1]], board[zero[0]][zero[1] -1] = board[zero[0]][zero[1]-1], board[zero[0]][zero[1]]
    res = ';'.join([' '.join(board[x]) for x in range(3)])
    return res


def possible_moves(_board):
    res = []
    zero_index = (0, 0)
    board = _board
    _board = []
    for row in board.split(';'):
        _board.append(row.split(' '))
    for i in range(len(_board)):
        if '0' in _board[i]:
            zero_index = (i, _board[i].index('0'))
    for move in moves[zero_index]:
        yield move_piece(deepcopy(_board), move, zero_index)

def IDS(src, dest, limit):
    visited = {src:1}
    for i in range(limit):
        if ids(src, dest, i, limit, visited):
            return 'Done'
    return 'Fail'

def ids(src, dest, limit, i, visited):
    #print('This is a new recursive call')
    #print('Src:', src)
    #print('Limit:', limit)
    if src == dest:
        return True
    if limit <= 0 or limit == i:
        return False
    for child in possible_moves(src):
        #print('Im src:', src, 'Im child:', child)
        if visited.get(child):
            visited[child] = min(limit, visited[child])
            continue
        if child == dest:
            print('Path found after', limit, 'movements')
            return True
        if child == src:
            return False
        visited[child] = limit+1
        #print('Visited:', visited)
        if ids(child, dest, limit+1, i, visited):
            return True

# source = '1 2 3;4 8 6;7 0 5'
source = '1 2 3;4 5 6;7 0 8'
source1 = '1 3 2;4 8 0;5 6 7'
source2 = '1 2 3;4 0 6;7 5 8'
# source = '1 2 3;0 4 6;7 5 8'
solution = '1 2 3;4 5 6;7 8 0'


moves = {
    (0, 0): ['down', 'right'],
    (0, 1): ['down', 'right', 'left'],
    (0, 2): ['down', 'left'],
    (1, 0): ['down', 'right', 'up'],
    (1, 1): ['down', 'right', 'left', 'up'],
    (1, 2): ['down', 'left', 'up'],
    (2, 0): ['up', 'right'],
    (2, 1): ['up', 'right', 'left'],
    (2, 2): ['up', 'left'],
}

print(IDS(source, solution, 2))
print(IDS(source1, solution, 800))
print(IDS(source2, solution, 800))