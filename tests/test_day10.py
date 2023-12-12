from src.utils import get_input
from src.day10 import part1, part2

def test_day10_part1_example():
    inputs = get_input("inputs/day10/day10_example.txt")
    assert part1(inputs) == 4

def test_day10_part1_example2():
    inputs = get_input("inputs/day10/day10_example2.txt")
    assert part1(inputs) == 8

def test_day10_part1():
    inputs = get_input("inputs/day10/day10.txt")
    assert part1(inputs) == 6754

def test_day10_part2_example1():
    inputs = get_input("inputs/day10/day10_part2_example1.txt")
    assert part2(inputs) == 4

def test_day10_part2_example2():
    inputs = get_input("inputs/day10/day10_part2_example2.txt")
    assert part2(inputs) == 8

def test_day10_part2_example3():
    inputs = get_input("inputs/day10/day10_part2_example3.txt")
    assert part2(inputs) == 10

def test_day10_part2():
    inputs = get_input("inputs/day10/day10.txt")
    assert part2(inputs) == 564