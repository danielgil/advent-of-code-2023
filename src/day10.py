import sys
from copy import deepcopy
from enum import Enum

class Direction(Enum):
    N = 1
    W = 2
    E = 3
    S = 4

def part1(input):
    sys.setrecursionlimit(20000)
    ground = [list(line) for line in input]
    start_position = find_start(ground)

    print(f"Starting at {start_position}")
    result = 0
    try:
        print("Trying N")
        visited_nodes = set()
        result = get_loop(ground, get_node(ground, start_position, Direction.N), start_position, visited_nodes)
    except ValueError:
        pass
    try:
        print("Trying W")
        visited_nodes = set()
        result = get_loop(ground, get_node(ground, start_position, Direction.W), start_position, visited_nodes)
    except ValueError:
        pass
    try:
        print("Trying E")
        visited_nodes = set()
        result = get_loop(ground, get_node(ground, start_position, Direction.E), start_position, visited_nodes)
    except ValueError:
        pass
    try:
        print("Trying S")
        visited_nodes = set()
        result = get_loop(ground, get_node(ground, start_position, Direction.S), start_position, visited_nodes)
    except ValueError:
        pass

    return result // 2


def part2(input):
    ground = [list(line) for line in input]
    loop_nodes = get_loop_nodes(ground)
    inside_nodes = set()

    for row in range(len(ground)):
        for column in range(len(ground[0])):
            node = (row, column)
            if node not in loop_nodes:
                if is_node_inside(ground, loop_nodes, node):
                    inside_nodes.add(node)

    print_ground(ground, loop_nodes, inside_nodes)
    return len(inside_nodes)


def is_node_inside(ground, loop_nodes, node):

    half_intersection = ""
    inside = False

    for column in range(node[1]):
        if (node[0], column) in loop_nodes:
            node_pipe = ground[node[0]][column]

            if node_pipe == "S":
                node_pipe = find_shape_of_start(ground, (node[0], column), loop_nodes)

            if node_pipe == "|" or node_pipe == half_intersection:
                inside = not inside
            if node_pipe == "F":
                half_intersection = "J"
            elif node_pipe == "L":
                half_intersection = "7"
            elif node_pipe != "-":
                half_intersection = ""
    return inside


def find_shape_of_start(ground, start, loop_nodes):

    north_node = get_node(ground, start, Direction.N)
    north_node_pipe = ground[north_node[0]][north_node[1]]
    south_node = get_node(ground, start, Direction.S)
    sout_node_pipe = ground[south_node[0]][south_node[1]]
    west_node = get_node(ground, start, Direction.W)
    west_node_pipe = ground[west_node[0]][west_node[1]]
    east_node = get_node(ground, start, Direction.E)
    east_node_pipe = ground[east_node[0]][east_node[1]]

    if (north_node in loop_nodes and north_node_pipe in ["|", "7", "F"]
            and south_node in loop_nodes and sout_node_pipe in ["|", "L", "J"]):
        return "|"
    if (north_node in loop_nodes and north_node_pipe in  ["|", "7", "F"]
            and east_node in loop_nodes and east_node_pipe in ["-", "J", "7"]):
        return "L"
    if (north_node in loop_nodes and north_node_pipe in ["|", "7", "F"]
            and west_node in loop_nodes and west_node_pipe in ["-", "F", "L"]):
        return "J"
    if (west_node in loop_nodes and west_node_pipe in ["-", "F", "L"]
            and east_node in loop_nodes and east_node_pipe in ["-", "J", "7"]):
        return "-"
    if (south_node in loop_nodes and sout_node_pipe in ["|", "L", "J"]
            and west_node in loop_nodes and west_node_pipe in ["-", "F", "L"]):
        return "7"
    if (south_node in loop_nodes and sout_node_pipe in ["|", "L", "J"]
            and east_node in loop_nodes and east_node_pipe in ["-", "J", "7"]):
        return "F"
    raise ValueError("Invalid start")

def get_loop_nodes(ground):
    sys.setrecursionlimit(20000)
    start_position = find_start(ground)

    marked_nodes = set()
    try:
        visited_nodes = set()
        get_loop_marking_ground(ground, get_node(ground, start_position, Direction.N), start_position, visited_nodes, marked_nodes)
        return marked_nodes
    except ValueError:
        pass
    try:
        visited_nodes = set()
        get_loop_marking_ground(ground, get_node(ground, start_position, Direction.W), start_position, visited_nodes, marked_nodes)
        return marked_nodes
    except ValueError:
        pass
    try:
        visited_nodes = set()
        get_loop_marking_ground(ground, get_node(ground, start_position, Direction.E), start_position, visited_nodes, marked_nodes)
        return marked_nodes
    except ValueError:
        pass
    try:
        visited_nodes = set()
        get_loop_marking_ground(ground, get_node(ground, start_position, Direction.S), start_position, visited_nodes, marked_nodes)
        return marked_nodes
    except ValueError:
        pass


def get_loop_marking_ground(ground, position, previous_position, visited_nodes, marked_nodes):
    if not position:
        raise ValueError("Dead end")
    if position in visited_nodes:
        raise ValueError("Cycle detected")
    current_pipe = ground[position[0]][position[1]]
    if current_pipe == "S":
        marked_nodes.add(position)
    if current_pipe == ".":
        raise ValueError("Dead end")

    next_position = follow_pipe(ground, position, previous_position)

    if next_position:
        visited_nodes.add(position)
        get_loop_marking_ground(ground, next_position, position, visited_nodes, marked_nodes)
        marked_nodes.add(position)


def get_loop(ground, position, previous_position, visited_nodes):
    if not position:
        raise ValueError("Dead end")
    if position in visited_nodes:
        print("cycle detected")
        raise ValueError("Cycle detected")
    current_pipe = ground[position[0]][position[1]]
    if current_pipe == "S":
        print(f"Found the start again at {position}")
        return 1
    if current_pipe == ".":
        raise ValueError("Dead end")

    next_position = follow_pipe(ground, position, previous_position)

    if next_position:
        print(f"  going from {position} to {next_position}")
        visited_nodes.add(position)
        return 1 + get_loop(ground, next_position, position, visited_nodes)
    else:
        print(f"  no next position from {position} and pipe '{current_pipe}'")


def follow_pipe(ground, position, previous_position):
    current_pipe = ground[position[0]][position[1]]
    next_position = None
    if current_pipe == "|":
        if previous_position == get_node(ground, position, Direction.N):
            next_position = get_node(ground, position, Direction.S)
        elif previous_position == get_node(ground, position, Direction.S):
            next_position = get_node(ground, position, Direction.N)
        else:
            raise ValueError("Broken pipe")
    elif current_pipe == "-":
        if previous_position == get_node(ground, position, Direction.W):
            next_position = get_node(ground, position, Direction.E)
        elif previous_position == get_node(ground, position, Direction.E):
            next_position = get_node(ground, position, Direction.W)
        else:
            raise ValueError("Broken pipe")
    elif current_pipe == "7":
        if previous_position == get_node(ground, position, Direction.W):
            next_position = get_node(ground, position, Direction.S)
        elif previous_position == get_node(ground, position, Direction.S):
            next_position = get_node(ground, position, Direction.W)
        else:
            raise ValueError("Broken pipe")
    elif current_pipe == "J":
        if previous_position == get_node(ground, position, Direction.W):
            next_position = get_node(ground, position, Direction.N)
        elif previous_position == get_node(ground, position, Direction.N):
            next_position = get_node(ground, position, Direction.W)
        else:
            raise ValueError("Broken pipe")
    elif current_pipe == "L":
        if previous_position == get_node(ground, position, Direction.N):
            next_position = get_node(ground, position, Direction.E)
        elif previous_position == get_node(ground, position, Direction.E):
            next_position = get_node(ground, position, Direction.N)
        else:
            raise ValueError("Broken pipe")
    elif current_pipe == "F":
        if previous_position == get_node(ground, position, Direction.S):
            next_position = get_node(ground, position, Direction.E)
        elif previous_position == get_node(ground, position, Direction.E):
            next_position = get_node(ground, position, Direction.S)
        else:
            raise ValueError("Broken pipe")
    return next_position


def find_start(ground):
    for row in range(len(ground)):
        for column in range(len(ground[0])):
            if ground[row][column] == "S":
                return (row, column)
    raise ValueError("No starting point")


def print_ground(ground, loop_nodes, enclosed_nodes):
    ground_copy = deepcopy(ground)
    for row in range(len(ground_copy)):
        for column in range(len(ground_copy[0])):
            node = (row, column)
            if node in loop_nodes:
                ground_copy[row][column] = "X"
            elif node in enclosed_nodes:
                ground_copy[row][column] = "O"
            else:
                ground_copy[row][column] = "."
    for line in ground_copy:
        print(" ".join(line))


def get_node(ground, node, direction):
    right_edge = len(ground[0]) - 1
    bottom_edge = len(ground) - 1
    if direction == Direction.N:
        if node[0] == 0:
            return None
        return (node[0] - 1, node[1])
    if direction == Direction.W:
        if node[1] == 0:
            return None
        return (node[0], node[1] - 1)
    if direction == Direction.E:
        if node[1] == right_edge:
            return None
        return (node[0], node[1] + 1)
    if direction == Direction.S:
        if node[0] == bottom_edge:
            return None
        return (node[0] + 1, node[1])
