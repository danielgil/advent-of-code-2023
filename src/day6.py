import re


def part1(data):
    times = [int(time) for time in re.findall(r'\d+', data[0])]
    distances = [int(distance) for distance in re.findall(r'\d+', data[1])]

    result = 1
    for race in range(len(times)):
        print(f"race {race}:")

        halfway = (times[race] // 2)
        print(f"  halfway = {halfway}")

        for time in range(halfway + 1):
            if time * (times[race] - time) > distances[race]:
                print(f"  first win at {time}")
                first_win = time
                break
        ways_to_win = ((halfway + 1 - first_win) * 2)
        if times[race] % 2 == 0:
            ways_to_win -= 1
        print(f"  ways to win race {race}: {ways_to_win}")
        result *= ways_to_win
    return result

def part2(data):
    time = int("".join(re.findall(r'\d+', data[0])))
    distance = int("".join(re.findall(r'\d+', data[1])))

    halfway = (time // 2)
    print(f"  halfway = {halfway}")

    for hold_time in range(halfway + 1):
        if hold_time * (time - hold_time) > distance:
            print(f"  first win at {hold_time}")
            first_win = hold_time
            break
    ways_to_win = ((halfway + 1 - first_win) * 2)
    if time % 2 == 0:
        ways_to_win -= 1
    print(f"  ways to win: {ways_to_win}")
    return ways_to_win
