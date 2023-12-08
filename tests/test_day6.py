from src.utils import get_input
from src.day6 import part1, part2

def test_day6_part1_example():
    inputs = get_input("inputs/day6/day6_example.txt")
    assert part1(inputs) == 288

def test_day6_part1_example():
    inputs = get_input("inputs/day6/day6.txt")
    assert part1(inputs) == 252000

def test_day6_part2_example():
    inputs = get_input("inputs/day6/day6_example.txt")
    assert part2(inputs) == 71503

def test_day6_part2():
    inputs = get_input("inputs/day6/day6.txt")
    assert part2(inputs) == 36992486