def part1(input):
    total = 0
    for line in input:
        parsed_line = [int(reading) for reading in line.split(" ")]
        print(parsed_line)
        total += get_next(parsed_line)
        print(f"{parsed_line}, {total}")

    print(f"total = {total}")
    return total

def part2(input):
    total = 0
    for line in input:
        parsed_line = [int(reading) for reading in line.split(" ")]
        print(parsed_line)
        reversed_line = list(reversed(parsed_line))
        total += get_next(reversed_line)
        print(f"{parsed_line}, {total}")

    print(f"total = {total}")
    return total

def get_next(history):
    if all_zeroes(history):
        return 0

    next_history = []
    for index in range(len(history) - 1):
        next_history.append(history[index + 1] - history[index])
    print(next_history)
    last_reading = history[-1] + get_next(next_history)
    return last_reading




def all_zeroes(history):
    for reading in history:
        if reading:
            return False
    return True