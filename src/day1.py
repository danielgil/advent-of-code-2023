def part1(input: str):
    result = 0
    for line in input:
        result += get_calibration_part1(line)
    return result


def part2(input: str):
    result = 0
    for line in input:
        result += get_calibration_part2(line)
    return result


def get_calibration_part1(input: str):

    for character in list(input):
        if character.isdigit():
            start = character
            break
    for character in reversed(list(input)):
        if character.isdigit():
            end = character
            break
    return int(start + end)


def get_calibration_part2(input: str):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    counters = dict.fromkeys(numbers.keys(), 0)

    start = None
    end = None

    print(f"line = {list(input)}")
    for character in list(input):
        if character.isdigit():
            counters = dict.fromkeys(numbers.keys(), 0)
            if start is None:
                print(f"start is now {character}")
                start = int(character)
            else:
                print(f"end is now {character}")
                end = int(character)
        else:
            for number in counters:
                current_index = counters[number]
                if character == number[current_index]:
                    counters[number] += 1
                elif character == number[0]:
                    counters[number] = 1
                else:
                    counters[number] = 0
                if counters[number] == len(number):
                    print(f"found a spelled number! {number} ({numbers[number]})")
                    counters[number] = 0
                    if start is None:
                        print(f"start is now {numbers[number]}")
                        start = numbers[number]
                    else:
                        print(f"end is now {numbers[number]}")
                        end = numbers[number]
    if not start:
        raise ValueError
    if not end:
        end = start
    print(f"calibration of {input} is {start * 10 + end}")
    return (start * 10) + end
