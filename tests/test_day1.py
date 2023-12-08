from src.day1 import part1, part2, get_calibration_part1, get_calibration_part2
from src.utils import get_input

def test_day1_calibration_part1():
    inputs = get_input("inputs/day1/day1_part1_example.txt")
    results = [12, 38, 15, 77]
    for x in range(len(inputs)):
        assert get_calibration_part1(inputs[x]) == results[x]

def test_day1_calibration_part2():
    inputs = get_input("inputs/day1/day1_part2_example.txt")

    results = [29, 83, 13, 24, 42, 14, 76]
    for x in range(len(inputs)):
        assert get_calibration_part2(inputs[x]) == results[x]

def test_day1_part1_example():
    inputs = get_input("inputs/day1/day1_part1_example.txt")
    assert part1(inputs) == 142

def test_day1_part2_example():
    inputs = get_input("inputs/day1/day1_part2_example.txt")
    assert part2(inputs) == 281

def test_day1_part1():
    inputs = get_input("inputs/day1/day1.txt")
    assert part1(inputs) == 55090

def test_day1_part2():
    inputs = get_input("inputs/day1/day1.txt")
    assert part2(inputs) == 54845
