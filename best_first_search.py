from random import choice
from copy import deepcopy

visited_nodes = []
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

start_state = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

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


def get_blank_tile(current_state):
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == 0:
                return i, j


def move_tile(current_state, blank_tile):
    """
    Tries all possible movements and returns the one with the least difference to
    the desired state
    """

    directions = {'left': move_left,
                  'up': move_up,
                  'down': move_down,
                  'right': move_right}
    directions = filter_possible_moves(blank_tile, directions)
    distances = dict()

    for direction in directions:
        distances[direction] = directions[direction](current_state, blank_tile)
    # print(distances)
    direction_to_call = get_min_value(distances)
    temp = deepcopy(current_state)
    directions[direction_to_call](temp, blank_tile, change_original=True)
    if temp in visited_nodes:
        del distances[direction_to_call]
        distances_iterator = iter(distances)
        new_direction = next(distances_iterator)
        directions[new_direction](current_state, blank_tile, change_original=True)
        new_board = deepcopy(current_state)
        visited_nodes.append(new_board)
    else:
        directions[direction_to_call](current_state, blank_tile, change_original=True)
        new_board = deepcopy(current_state)
        visited_nodes.append(new_board)


def filter_possible_moves(blank_tile, distances):
    new_distances = dict()
    possible_moves = moves[blank_tile]
    for move in possible_moves:
        new_distances[move] = distances[move]
    return new_distances


def move_left(current_state, blank, change_original=False):
    current_state[blank[0]][blank[1]], current_state[blank[0]][blank[1]-1] = \
        current_state[blank[0]][blank[1]-1], current_state[blank[0]][blank[1]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[blank[0]][blank[1]], current_state[blank[0]][blank[1]-1] = \
        current_state[blank[0]][blank[1]-1], current_state[blank[0]][blank[1]]
    return distance


def move_right(current_state, blank, change_original=False):
    current_state[blank[0]][blank[1]], current_state[blank[0]][blank[1] + 1] = \
        current_state[blank[0]][blank[1] + 1], current_state[blank[0]][blank[1]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[blank[0]][blank[1]], current_state[blank[0]][blank[1] + 1] = \
        current_state[blank[0]][blank[1] + 1], current_state[blank[0]][blank[1]]
    return distance


def move_up(current_state, blank, change_original=False):
    current_state[blank[0]][blank[1]], current_state[blank[0]-1][blank[1]] = \
        current_state[blank[0] - 1][blank[1]], current_state[blank[0]][blank[1]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[blank[0]][blank[1]], current_state[blank[0]-1][blank[1]] = \
        current_state[blank[0] - 1][blank[1]], current_state[blank[0]][blank[1]]
    return distance


def move_down(current_state, blank, change_original=False):
    current_state[blank[0]+1][blank[1]], current_state[blank[0]][blank[1]] = \
        current_state[blank[0]][blank[1]], current_state[blank[0] + 1][blank[1]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[blank[0]+1][blank[1]], current_state[blank[0]][blank[1]] = \
        current_state[blank[0]][blank[1]], current_state[blank[0] + 1][blank[1]]
    return distance


def get_distance_to_desire_state(current_state, desire_state):
    diff = 0
    for row_state, row_desire in zip(current_state, desire_state):
        diff_in_row = compare_rows(row_state, row_desire)
        diff += diff_in_row

    return diff


def compare_rows(row_state, row_desire):
    """
    compares each row in the puzzles, this fucntion is called by 'get_distance_to_desire_state
    """
    diff = 0
    for current_num, desire_num in zip(row_state, row_desire):
        if current_num != desire_num:
            diff += 1

    return diff


def get_min_value(distances_dictionary):
    current_min = 9
    direction = choice(list(distances_dictionary.keys()))
    for k in distances_dictionary:
        if distances_dictionary[k] < current_min:
            current_min = distances_dictionary[k]
            direction = k
    return direction


def play(current_state, desired_state, new_board):
    print(current_state)
    # for i in range(3):
    while current_state != desired_state:
        blank = get_blank_tile(current_state)
        move_tile(current_state, blank)
        print(current_state)


play(start_state, goal_state, move_tile(start_state, get_blank_tile(start_state)))

