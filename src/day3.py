import re
def part1(data):
    engine = [list(line) for line in data]
    size = len(engine)
    total = 0

    number_buffer = ''
    is_adjacent = False
    for row in range(size):
        for column in range(size):
            if engine[row][column].isdigit():
                number_buffer += engine[row][column]
                is_adjacent = is_adjacent or is_adjacent_to_symbol(engine, row, column)

            if not engine[row][column].isdigit() or column + 1 == size:
                if is_adjacent:
                    total += int(number_buffer)
                number_buffer = ''
                is_adjacent = False
    return total


def part2(data):
    engine = [list(line) for line in data]
    size = len(engine)
    total = 0
    gears = {}

    number_buffer = ''
    adjacent_gears = []
    for row in range(size):
        for column in range(size):
            if engine[row][column].isdigit():
                number_buffer += engine[row][column]
                adjacent_gears += get_adjacent_gear_positions(engine, row, column)

            if not engine[row][column].isdigit() or column + 1 == size:
                unique_adjacent_gears = set(adjacent_gears)
                for gear in unique_adjacent_gears:
                    if gear in gears:
                        gears[gear].append(int(number_buffer))
                    else:
                        gears[gear] = [int(number_buffer)]
                number_buffer = ''
                adjacent_gears = []

    for gear in gears:
        if len(gears[gear]) == 2:
            total += gears[gear][0] * gears[gear][1]
    return total


def is_adjacent_to_symbol(engine, row, column):
    size = len(engine)

    if row - 1 >= 0:
        # top left
        if column - 1 >= 0:
            if is_symbol(engine[row - 1][column - 1]):
                return True
        # top
        if is_symbol(engine[row - 1][column]):
            return True
        # top right
        if column + 1 < size:
            if is_symbol(engine[row - 1][column + 1]):
                return True
    # left
    if column - 1 >= 0:
        if is_symbol(engine[row][column - 1]):
            return True
    # right
    if column + 1 < size:
        if is_symbol(engine[row][column + 1]):
            return True

    if row + 1 < size:
        # bottom left
        if column - 1 >= 0:
            if is_symbol(engine[row + 1][column - 1]):
                return True
        # bottom
        if is_symbol(engine[row + 1][column]):
            return True
        # bottom right
        if column + 1 < size:
            if is_symbol(engine[row + 1][column + 1]):
                return True
    return False


def is_symbol(char: str):
    return len(char) == 1 and not char.isalnum() and char != "."

def is_gear(char: str):
    return len(char) == 1 and char == "*"

def get_adjacent_gear_positions(engine, row, column):
    size = len(engine)
    gear_positions = []

    if row - 1 >= 0:
        # top left
        if column - 1 >= 0:
            if is_gear(engine[row - 1][column - 1]):
                gear_positions.append((row -1, column - 1))
        # top
        if is_gear(engine[row - 1][column]):
            gear_positions.append((row -1, column))

        # top right
        if column + 1 < size:
            if is_gear(engine[row - 1][column + 1]):
                gear_positions.append((row -1, column + 1))
    # left
    if column - 1 >= 0:
        if is_gear(engine[row][column - 1]):
            gear_positions.append((row, column - 1))
    # right
    if column + 1 < size:
        if is_gear(engine[row][column + 1]):
            gear_positions.append((row, column + 1))

    if row + 1 < size:
        # bottom left
        if column - 1 >= 0:
            if is_gear(engine[row + 1][column - 1]):
                gear_positions.append((row + 1, column -1))
        # bottom
        if is_gear(engine[row + 1][column]):
            gear_positions.append((row + 1, column))
        # bottom right
        if column + 1 < size:
            if is_gear(engine[row + 1][column + 1]):
                gear_positions.append((row + 1, column + 1))
    return gear_positions

def get_gear_ratio(engine, row, column):
    size = len(engine)

    if row - 1 >= 0:
        # top left
        if column - 1 >= 0:
            if is_symbol(engine[row - 1][column - 1]):
                return True
        # top
        if is_symbol(engine[row - 1][column]):
            return True
        # top right
        if column + 1 < size:
            if is_symbol(engine[row - 1][column + 1]):
                return True
    # left
    if column - 1 >= 0:
        if is_symbol(engine[row][column - 1]):
            return True
    # right
    if column + 1 < size:
        if is_symbol(engine[row][column + 1]):
            return True

    if row + 1 < size:
        # bottom left
        if column - 1 >= 0:
            if is_symbol(engine[row + 1][column - 1]):
                return True
        # bottom
        if is_symbol(engine[row + 1][column]):
            return True
        # bottom right
        if column + 1 < size:
            if is_symbol(engine[row + 1][column + 1]):
                return True
    return False