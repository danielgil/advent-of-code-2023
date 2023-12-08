from src.utils import get_input
from src.day2 import part1, part2


def test_day2_part1_example():
    inputs = get_input("inputs/day2/day2_part1_example.txt")
    assert part1(inputs) == 8


def test_day2_part1():
    inputs = get_input("inputs/day2/day2.txt")
    assert part1(inputs) == 2162


def test_day2_part2_example():
    inputs = get_input("inputs/day2/day2_part1_example.txt")
    assert part2(inputs) == 2286


def test_day2_part2():
    inputs = get_input("inputs/day2/day2.txt")
    assert part2(inputs) == 72513
