goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

start_state = [
    [2, 5, 6],
    [1, 0, 7],
    [8, 3, 4]
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

adjacency = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(1, 0), (0, 1), (1, 2), (2, 1)],
    (1, 2): [(1, 1), (0, 2), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(2, 0), (1, 1), (2, 2)],
    (2, 2): [(2, 1), (1, 2)]
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

    distances = {'left': move_left(current_state, blank_tile),
                 'up': move_up(current_state, blank_tile),
                 'down': move_down(current_state, blank_tile),
                 'right': move_right(current_state, blank_tile)}
    direction_to_call = get_min_value(distances)
    directions[direction_to_call](current_state,blank_tile, change_original=True)


def move_left(current_state, blank_tile, change_original=False):
    current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]-1]] = \
        current_state[[blank_tile[0]], [blank_tile[1]-1]], current_state[[blank_tile[0]], [blank_tile[1]]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]-1]] = \
        current_state[[blank_tile[0]], [blank_tile[1]-1]], current_state[[blank_tile[0]], [blank_tile[1]]]
    return distance


def move_right(current_state, blank_tile, change_original=False):
    current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]+1]] = \
        current_state[[blank_tile[0]], [blank_tile[1]+1]], current_state[[blank_tile[0]], [blank_tile[1]]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1] + 1]] = \
        current_state[[blank_tile[0]], [blank_tile[1] + 1]], current_state[[blank_tile[0]], [blank_tile[1]]]
    return distance


def move_up(current_state, blank_tile, change_original=False):
    current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]-1]] = \
        current_state[[blank_tile[0]-1], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1] - 1]] = \
        current_state[[blank_tile[0] - 1], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]]]
    return distance


def move_down(current_state, blank_tile, change_original=False):
    current_state[[blank_tile[0]+1], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]]] = \
        current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0]+1], [blank_tile[1]]]
    distance = get_distance_to_desire_state(current_state, goal_state)

    if change_original:
        return None

    current_state[[blank_tile[0] + 1], [blank_tile[1]]], current_state[[blank_tile[0]], [blank_tile[1]]] = \
        current_state[[blank_tile[0]], [blank_tile[1]]], current_state[[blank_tile[0] + 1], [blank_tile[1]]]
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
    for k in distances_dictionary:
        if distances_dictionary[k] < current_min:
            current_min = distances_dictionary[k]
            direction = k
            return direction


print(start_state)
move_tile(start_state, get_blank_tile(start_state))
print(start_state)
