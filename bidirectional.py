from copy import deepcopy

def move_piece(board, direction, zero, size):
    if direction == 'up':
        board[zero[0]][zero[1]], board[zero[0]-1][zero[1]] = board[zero[0]-1][zero[1]], board[zero[0]][zero[1]]
    elif direction == 'down':
        board[zero[0]][zero[1]], board[zero[0]+1][zero[1]] = board[zero[0]+1][zero[1]], board[zero[0]][zero[1]]
    elif direction == 'right':
        board[zero[0]][zero[1]], board[zero[0]][zero[1]+1] = board[zero[0]][zero[1]+1], board[zero[0]][zero[1]]
    elif direction == 'left':
        board[zero[0]][zero[1]], board[zero[0]][zero[1]-1] = board[zero[0]][zero[1]-1], board[zero[0]][zero[1]]
    res = ';'.join([' '.join(board[x]) for x in range(size)])
    return res

def possible_moves(_board, size):
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
        yield move_piece(deepcopy(_board), move, zero_index, size)

def bds(src, goal, size):
    visitados_src = {}
    visitados_goal = {}

    stack_src = [src]
    visitados_src[src] = 1
    stack_goal = [goal]
    visitados_goal[goal] = 1
    i = 0
    while stack_goal and stack_src:
        i += 1
        if stack_src:
            cur_node_src = stack_src.pop()
            if cur_node_src == goal:
                print('We have finished after', i, 'movements')
                stack_src.clear()
                stack_goal.clear()
                break
            for child in possible_moves(cur_node_src, size):
                if visitados_goal.get(child):
                    print('We have finished after', i, 'movements')
                    stack_src.clear()
                    stack_goal.clear()
                    break
                if visitados_src.get(child):
                    if visitados_goal.get(child):
                        print('We have finished after', i, 'movements')
                        stack_src.clear()
                        stack_goal.clear()
                        break
                else:
                    visitados_src[child] = 1
                    stack_src.append(child)
        if stack_goal:
            cur_node_goal = stack_goal.pop()
            if cur_node_goal == src:
                print('We have finished after', i, 'movements')
                stack_src.clear()
                stack_goal.clear()
                break
            for child_goal in possible_moves(cur_node_goal, size):
                if visitados_src.get(child_goal):
                    print('We have finished after', i, 'movements')
                    stack_src.clear()
                    stack_goal.clear()
                    break
                if visitados_goal.get(child_goal):
                    if visitados_src.get(child_goal):
                        print('We have finished after', i, 'movements')
                        stack_src.clear()
                        stack_goal.clear()
                        break
                else:
                    visitados_goal[child_goal] = 1
                    stack_goal.append(child_goal)
    return 'Not solvable'

source1 = '1 3 2;4 8 0;5 6 7'
source = '1 2 3;4 0 6;7 5 8'
solution = '1 2 3;4 5 6;7 8 0'

# solution = '15 14 13 12;11 10 9 8;7 6 5 4;3 2 1 0'
# source1 = '1 2 3 4;5 6 7 8;9 10 11 12;13 14 15 0'

moves = {
    (0, 0) : ['down', 'right'],
    (0, 1) : ['down', 'right', 'left'],
    (0, 2) : ['down', 'left'],
    (1, 0) : ['down', 'right', 'up'],
    (1, 1) : ['down', 'right', 'left', 'up'],
    (1, 2) : ['down', 'left', 'up'],
    (2, 0) : ['up', 'right'],
    (2, 1) : ['up', 'right', 'left'],
    (2, 2) : ['up', 'left'],
}

moves4x4 = {
    (0, 0) : ['down', 'right'],
    (0, 1) : ['down', 'right', 'left'],
    (0, 2) : ['down', 'left'],
    (0, 3) : ['down', 'right', 'up'],
    (1, 0) : ['down', 'right', 'left', 'up'],
    (1, 1) : ['down', 'left', 'up'],
    (1, 2) : ['up', 'right'],
    (1, 3) : ['up', 'right', 'left'],
    (2, 0) : ['up', 'left'],
    (2, 1) : ['up', 'left'],
    (2, 2) : ['up', 'left'],
    (2, 3) : ['up', 'left'],
    (3, 0) : ['up', 'left'],
    (3, 1) : ['up', 'left'],
    (3, 2) : ['up', 'left'],
    (3, 3) : ['up', 'left'],
}

bds(source1, solution, 3)