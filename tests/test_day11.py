from src.utils import get_input
from src.day11 import part1, part2

def test_day11_part1_example():
    inputs = get_input("inputs/day11/day11_example.txt")
    assert part1(inputs) == 374

def test_day11_part1():
    inputs = get_input("inputs/day11/day11.txt")
    assert part1(inputs) == 10033566

def test_day11_part2_example():
    inputs = get_input("inputs/day11/day11_example.txt")
    assert part2(inputs) == 8410

def test_day11_part2():
    inputs = get_input("inputs/day11/day11.txt")
    assert part2(inputs) == 0