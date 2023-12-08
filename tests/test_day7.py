from src.utils import get_input
from src.day7 import part1, part2

def test_day7_part1_example():
    inputs = get_input("inputs/day7/day7_example.txt")
    assert part1(inputs) == 6440

def test_day7_part1():
    inputs = get_input("inputs/day7/day7.txt")
    assert part1(inputs) == 248422077

def test_day7_part2_example():
    inputs = get_input("inputs/day7/day7_example.txt")
    assert part2(inputs) == 5905

def test_day7_part1():
    inputs = get_input("inputs/day7/day7.txt")
    assert part2(inputs) == 249817836