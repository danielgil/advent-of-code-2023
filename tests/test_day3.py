from src.utils import get_input
from src.day3 import part1, part2


def test_day3_part1_example():
    inputs = get_input("inputs/day3/day3_example.txt")
    assert part1(inputs) == 4361

def test_day3_part1():
    inputs = get_input("inputs/day3/day3.txt")
    assert part1(inputs) == 537832

def test_day3_part2_example():
    inputs = get_input("inputs/day3/day3_example.txt")
    assert part2(inputs) == 467835

def test_day3_part2():
    inputs = get_input("inputs/day3/day3.txt")
    assert part2(inputs) == 81939900