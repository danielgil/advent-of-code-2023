from src.utils import get_input
from src.day4 import part1, part2

def test_day4_part1_example():
    inputs = get_input("inputs/day4/day4_example.txt")
    assert part1(inputs) == 13

def test_day4_part1():
    inputs = get_input("inputs/day4/day4.txt")
    assert part1(inputs) == 23847

def test_day4_part2_example():
    inputs = get_input("inputs/day4/day4_example.txt")
    assert part2(inputs) == 30

def test_day4_part2():
    inputs = get_input("inputs/day4/day4.txt")
    assert part2(inputs) == 8570000

