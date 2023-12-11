from src.utils import get_input
from src.day9 import part1, part2

def test_day9_part1_example():
    inputs = get_input("inputs/day9/day9_example.txt")
    assert part1(inputs) == 114

def test_day9_part1():
    inputs = get_input("inputs/day9/day9.txt")
    assert part1(inputs) == 1955513104

def test_day9_part2_example():
    inputs = get_input("inputs/day9/day9_example.txt")
    assert part2(inputs) == 2

def test_day9_part2():
    inputs = get_input("inputs/day9/day9.txt")
    assert part2(inputs) == 1131