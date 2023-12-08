from src.utils import get_input
from src.day8 import part1, part2

def test_day8_part1_example():
    inputs = get_input("inputs/day8/day8_example.txt")
    assert part1(inputs) == 6

def test_day8_part1():
    inputs = get_input("inputs/day8/day8.txt")
    assert part1(inputs) == 15871

def test_day8_part2_example():
    inputs = get_input("inputs/day8/day8_part2_example.txt")
    assert part2(inputs) == 6

def test_day8_part2():
    inputs = get_input("inputs/day8/day8.txt")
    assert part2(inputs) == 11283670395017